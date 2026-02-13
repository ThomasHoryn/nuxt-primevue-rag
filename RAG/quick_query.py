#!/usr/bin/env python3
"""
Quick RAG Query - CLI wrapper for automated workflows
Usage: python3 quick_query.py "Your question" --db primevue|nuxt|both
"""

import argparse
import sys
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Configuration
TOP_K = 7
DATABASES = {
    'primevue': {
        'path': './chroma_db_primevue',
        'name': 'PrimeVue'
    },
    'nuxt': {
        'path': './chroma_db_nuxt',
        'name': 'Nuxt'
    }
}

def load_vectorstore(db_name):
    """Load vector database"""
    if db_name not in DATABASES:
        raise ValueError(f"Unknown database: {db_name}")

    print(f"📖 Ładowanie bazy: {DATABASES[db_name]['name']}...", file=sys.stderr)
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory=DATABASES[db_name]['path'],
        embedding_function=embeddings
    )
    return vectorstore, DATABASES[db_name]['name']

def generate_prompt(question, db_choice):
    """Generate RAG prompt from question and database choice"""

    # Load databases
    vectorstores = []
    if db_choice == 'both':
        for db in ['primevue', 'nuxt']:
            vs, name = load_vectorstore(db)
            vectorstores.append((vs, name, db))
    else:
        vs, name = load_vectorstore(db_choice)
        vectorstores.append((vs, name, db_choice))

    # Collect fragments
    all_fragments = []
    for vectorstore, framework_name, db_key in vectorstores:
        print(f"🧠 Wyszukiwanie w dokumentacji {framework_name}...", file=sys.stderr)
        docs = vectorstore.similarity_search(question, k=TOP_K)

        for doc in docs:
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
                'framework': framework_name
            })

    # Build prompt
    frameworks = list(set([f['framework'] for f in all_fragments]))
    if len(frameworks) > 1:
        role = "You are an expert coding assistant for Nuxt and PrimeVue"
    else:
        role = f"You are an expert coding assistant specialized in {frameworks[0]}"

    context_parts = []
    for i, fragment in enumerate(all_fragments, 1):
        context_parts.append(f"Fragment {i}:")
        context_parts.append(f"Źródło: {fragment['source']}")
        context_parts.append(fragment['content'])
        context_parts.append("")

    context = "\n".join(context_parts)

    critical_rules = """CRITICAL RULES:
1. NO OUTSIDE KNOWLEDGE - Use ONLY information from the <context> fragments above
2. CITATION MANDATORY - Always cite sources using "Źródło: [Framework] - [Header path]"
3. COMPOSITION API - Use Vue 3 Composition API with <script setup> syntax
4. NO HALLUCINATION - If information is not in context, say "I don't have that information in the provided context\""""

    final_output = f"""{role}.

<context>
{context}
</context>

<question>
{question}
</question>

{critical_rules}

Provide a comprehensive answer based strictly on the context above."""

    return final_output

def main():
    parser = argparse.ArgumentParser(
        description='Quick RAG Query - Get contextual prompts for GitHub Copilot',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 quick_query.py "How to use DataTable?" --db primevue
  python3 quick_query.py "useState in Nuxt 3" --db nuxt
  python3 quick_query.py "useFetch with DataTable" --db both
        """
    )

    parser.add_argument('question', help='Your question about Nuxt/PrimeVue')
    parser.add_argument(
        '--db',
        choices=['primevue', 'nuxt', 'both'],
        default='both',
        help='Documentation source to query (default: both)'
    )
    parser.add_argument(
        '--copy',
        action='store_true',
        help='Copy result to clipboard (requires xclip or xsel)'
    )

    args = parser.parse_args()

    try:
        print(f"\n{'='*80}", file=sys.stderr)
        print(f"❓ Pytanie: {args.question}", file=sys.stderr)
        print(f"📚 Źródło: {args.db}", file=sys.stderr)
        print(f"{'='*80}\n", file=sys.stderr)

        # Generate prompt
        prompt = generate_prompt(args.question, args.db)

        # Output prompt
        print("\n" + "="*80)
        print("SKOPIUJ PONIŻSZY PROMPT DO GITHUB COPILOT CHAT")
        print("="*80 + "\n")
        print(prompt)
        print("\n" + "="*80)
        print("Wklej do GitHub Copilot Chat: Ctrl+Alt+I")
        print("="*80 + "\n")

        # Try to copy to clipboard
        if args.copy:
            try:
                import subprocess
                subprocess.run(['xclip', '-selection', 'clipboard'],
                             input=prompt.encode(), check=True)
                print("✅ Skopiowano do schowka!", file=sys.stderr)
            except (subprocess.CalledProcessError, FileNotFoundError):
                try:
                    subprocess.run(['xsel', '--clipboard', '--input'],
                                 input=prompt.encode(), check=True)
                    print("✅ Skopiowano do schowka!", file=sys.stderr)
                except:
                    print("⚠️  Nie można skopiować (zainstaluj xclip lub xsel)", file=sys.stderr)

    except Exception as e:
        print(f"\n❌ Błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
