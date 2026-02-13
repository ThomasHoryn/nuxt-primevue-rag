"""
RAG Documentation Indexer
Builds vector database from documentation files with batch processing and progress tracking.
"""

import os
import argparse
from typing import List
from tqdm import tqdm
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_core.documents import Document

# Import configuration
from config import (
    DB_PATHS,
    EMBEDDING_MODEL_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    HEADERS_TO_SPLIT_ON,
    BATCH_SIZE
)


def build_index(db_name: str) -> None:
    """
    Build vector database index from documentation file.

    Args:
        db_name: Name of the database to build (primevue, nuxt)
    """
    if db_name not in DB_PATHS:
        raise ValueError(f"Unknown database: {db_name}. Available: {list(DB_PATHS.keys())}")

    db_info = DB_PATHS[db_name]
    file_path = db_info['source_file']
    db_path = db_info['path']
    db_display_name = db_info['name']

    print(f"1. 📖 Loading {file_path}...")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Step A: Split by Markdown headers to preserve section context
    print("2. 📄 Splitting document into sections...")
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=HEADERS_TO_SPLIT_ON)
    md_header_splits = markdown_splitter.split_text(text)
    print(f"   ✓ Found {len(md_header_splits)} logical Markdown sections.")

    # Step B: Further split long sections while preserving header metadata
    print("3. ✂️  Splitting long sections into smaller chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""]
    )
    final_splits: List[Document] = text_splitter.split_documents(md_header_splits)
    print(f"   ✓ Created {len(final_splits)} final chunks (with header context).")

    # Step C: Generate embeddings with batch processing
    print(f"4. 🧠 Creating embeddings (model: {EMBEDDING_MODEL_NAME})...")
    print(f"   Processing in batches of {BATCH_SIZE} documents...")

    embedding_function = SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # Process in batches with progress bar
    vectorstore = None
    for i in tqdm(range(0, len(final_splits), BATCH_SIZE), desc="Indexing"):
        batch = final_splits[i:i + BATCH_SIZE]

        if vectorstore is None:
            # Create new database with first batch
            vectorstore = Chroma.from_documents(
                documents=batch,
                embedding=embedding_function,
                persist_directory=db_path
            )
        else:
            # Add subsequent batches
            vectorstore.add_documents(batch)

    print(f"✅ Success! Database {db_display_name} saved in {db_path}")
    print(f"   Total number of documents: {len(final_splits)}")


def main() -> None:
    """Main entry point for the indexer."""
    parser = argparse.ArgumentParser(
        description='Build RAG vector database from documentation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Index single database
  python3 index_db.py --db primevue
  python3 index_db.py --db nuxt

  # Index all databases
  python3 index_db.py --all
        """
    )

    parser.add_argument(
        '--db',
        choices=list(DB_PATHS.keys()),
        help='Database to build'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Build all databases'
    )

    args = parser.parse_args()

    if not args.db and not args.all:
        parser.error("Specify either --db or --all")

    try:
        if args.all:
            print(f"\n{'='*80}")
            print("Building all databases...")
            print(f"{'='*80}\n")
            for db_name in DB_PATHS.keys():
                print(f"\n--- Database: {DB_PATHS[db_name]['name']} ---\n")
                build_index(db_name)
                print()
        else:
            build_index(args.db)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)


if __name__ == "__main__":
    main()
