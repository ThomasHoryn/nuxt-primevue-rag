#!/usr/bin/env python3
"""
Quick RAG Query - Unified CLI and interactive tool for RAG queries
Usage:
  CLI mode: python3 quick_query.py "Your question" --db primevue|nuxt|both
  Interactive mode: python3 quick_query.py --interactive
"""

import argparse
import html
import os
import sys
from typing import List, Dict, Tuple, Optional, Any
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_core.documents import Document

# Import configuration
from config import DB_PATHS, EMBEDDING_MODEL_NAME, TOP_K


def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent XML/prompt injection attacks.

    Args:
        text: User input to sanitize

    Returns:
        Sanitized text with escaped XML characters
    """
    return html.escape(text, quote=False)


def load_vectorstore(db_name: str, embedding_function: SentenceTransformerEmbeddings) -> Tuple[Chroma, str]:
    """
    Load vector database.

    Args:
        db_name: Database name (primevue, nuxt)
        embedding_function: Pre-initialized embedding model

    Returns:
        Tuple of (vectorstore, framework_name)
    """
    if db_name not in DB_PATHS:
        raise ValueError(f"Unknown database: {db_name}. Available: {list(DB_PATHS.keys())}")

    db_info = DB_PATHS[db_name]
    print(f"📖 Loading database: {db_info['name']}...", file=sys.stderr)

    vectorstore = Chroma(
        persist_directory=db_info['path'],
        embedding_function=embedding_function
    )
    return vectorstore, db_info['name']


def retrieve_with_scores(
    vectorstore: Chroma,
    question: str,
    framework_name: str,
    k: int = TOP_K
) -> List[Tuple[Document, float, str]]:
    """
    Retrieve documents with similarity scores.

    Args:
        vectorstore: ChromaDB vectorstore
        question: Query string
        framework_name: Name of the framework (for metadata)
        k: Number of results to retrieve

    Returns:
        List of (document, score, framework_name) tuples
    """
    docs_with_scores = vectorstore.similarity_search_with_score(question, k=k)
    return [(doc, score, framework_name) for doc, score in docs_with_scores]


def generate_prompt(question: str, db_choice: str, embedding_function: SentenceTransformerEmbeddings) -> str:
    """
    Generate RAG prompt from question and database choice.

    Args:
        question: User question (will be sanitized)
        db_choice: Database choice (primevue, nuxt, both)
        embedding_function: Pre-initialized embedding model

    Returns:
        Complete prompt string ready for LLM
    """
    # Sanitize input to prevent prompt injection
    safe_question = sanitize_input(question)

    # Load databases
    docs_with_scores: List[Tuple[Document, float, str]] = []

    if db_choice == 'both':
        for db in ['primevue', 'nuxt']:
            vs, name = load_vectorstore(db, embedding_function)
            print(f"🧠 Searching in {name} documentation...", file=sys.stderr)
            docs_with_scores.extend(retrieve_with_scores(vs, question, name, k=TOP_K))

        # Sort by score (lower is better for distance metrics) and take top results
        docs_with_scores.sort(key=lambda x: x[1])
        docs_with_scores = docs_with_scores[:TOP_K * 2]  # Keep top results from both
    else:
        vs, name = load_vectorstore(db_choice, embedding_function)
        print(f"🧠 Searching in {name} documentation...", file=sys.stderr)
        docs_with_scores = retrieve_with_scores(vs, question, name, k=TOP_K)

    # Build fragments list
    all_fragments: List[Dict[str, Any]] = []
    frameworks = set()

    for doc, score, framework_name in docs_with_scores:
        frameworks.add(framework_name)
        metadata = doc.metadata
        headers = []
        for i in range(1, 4):
            header_key = f'Header_{i}'
            if header_key in metadata and metadata[header_key]:
                headers.append(metadata[header_key])

        source = f"{framework_name} - {' > '.join(headers)}" if headers else framework_name
        all_fragments.append({
            'content': doc.page_content,
            'source': source,
            'framework': framework_name,
            'score': score
        })

    # Build prompt
    if len(frameworks) > 1:
        role = "You are an expert coding assistant for Nuxt and PrimeVue"
    else:
        role = f"You are an expert coding assistant specialized in {list(frameworks)[0]}"

    context_parts = []
    for i, fragment in enumerate(all_fragments, 1):
        context_parts.append(f"Fragment {i}:")
        context_parts.append(f"Source: {fragment['source']}")
        context_parts.append(fragment['content'])
        context_parts.append("")

    context = "\n".join(context_parts)

    critical_rules = """CRITICAL RULES:
1. NO OUTSIDE KNOWLEDGE - Use ONLY information from the <context> fragments above
2. CITATION MANDATORY - Always cite sources using "Source: [Framework] - [Header path]"
3. COMPOSITION API - Use Vue 3 Composition API with <script setup> syntax
4. NO HALLUCINATION - If information is not in context, say "I don't have that information in the provided context\""""

    final_output = f"""{role}.

<context>
{context}
</context>

<question>
{safe_question}
</question>

{critical_rules}

Provide a comprehensive answer based strictly on the context above."""

    return final_output


def interactive_mode(embedding_function: SentenceTransformerEmbeddings) -> None:
    """
    Interactive mode for continuous queries.

    Args:
        embedding_function: Pre-initialized embedding model
    """
    print("\n🎯 RAG Interactive Mode")
    print("="*80)
    print("Available databases: PrimeVue, Nuxt, Both")
    print("Type 'exit' or 'quit' to exit")
    print("="*80 + "\n")

    while True:
        try:
            db_choice = input("📚 Select database (primevue/nuxt/both): ").strip().lower()
            if db_choice in ['exit', 'quit']:
                break
            if db_choice not in ['primevue', 'nuxt', 'both']:
                print("❌ Invalid choice! Available: primevue, nuxt, both")
                continue

            question = input("🔎 Your question: ").strip()
            if not question:
                continue
            if question.lower() in ['exit', 'quit']:
                break

            print(f"\n{'='*80}")
            prompt = generate_prompt(question, db_choice, embedding_function)
            print(f"{'='*80}")
            print("COPY THE PROMPT BELOW TO GITHUB COPILOT CHAT")
            print(f"{'='*80}\n")
            print(prompt)
            print(f"\n{'='*80}\n")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}", file=sys.stderr)


def copy_to_clipboard(text: str) -> bool:
    """
    Copy text to clipboard using cross-platform library.

    Args:
        text: Text to copy

    Returns:
        True if successful, False otherwise
    """
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except ImportError:
        print("⚠️  pyperclip is not installed. Run: pip install pyperclip", file=sys.stderr)
        return False
    except Exception as e:
        print(f"⚠️  Cannot copy to clipboard: {e}", file=sys.stderr)
        return False


def main() -> None:
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description='Quick RAG Query - Get contextual prompts for GitHub Copilot',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # CLI mode
  python3 quick_query.py "How to use DataTable?" --db primevue
  python3 quick_query.py "useState in Nuxt 3" --db nuxt
  python3 quick_query.py "useFetch with DataTable" --db both --copy

  # Interactive mode
  python3 quick_query.py --interactive
        """
    )

    parser.add_argument(
        'question',
        nargs='?',
        help='Your question about Nuxt/PrimeVue (not needed in interactive mode)'
    )
    parser.add_argument(
        '--db',
        choices=['primevue', 'nuxt', 'both'],
        default='both',
        help='Documentation source to query (default: both)'
    )
    parser.add_argument(
        '--copy',
        action='store_true',
        help='Copy result to clipboard (requires pyperclip)'
    )
    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run in interactive mode for continuous queries'
    )

    args = parser.parse_args()

    # Initialize embedding model once (expensive operation)
    print("🧠 Initializing embedding model...", file=sys.stderr)
    embedding_function = SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    try:
        if args.interactive:
            # Interactive mode
            interactive_mode(embedding_function)
        else:
            # CLI mode
            if not args.question:
                parser.error("question is required in CLI mode (or use --interactive)")

            print(f"\n{'='*80}", file=sys.stderr)
            print(f"❓ Question: {args.question}", file=sys.stderr)
            print(f"📚 Source: {args.db}", file=sys.stderr)
            print(f"{'='*80}\n", file=sys.stderr)

            # Generate prompt
            prompt = generate_prompt(args.question, args.db, embedding_function)

            # Output prompt
            print("\n" + "="*80)
            print("COPY THE PROMPT BELOW TO GITHUB COPILOT CHAT")
            print("="*80 + "\n")
            print(prompt)
            print("\n" + "="*80)
            print("Paste into GitHub Copilot Chat: Ctrl+Alt+I")
            print("="*80 + "\n")

            # Try to copy to clipboard
            if args.copy:
                if copy_to_clipboard(prompt):
                    print("✅ Copied to clipboard!", file=sys.stderr)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
