"""
Configuration constants for the RAG system.
Centralizes all paths, model names, and parameters.
"""
import os
from typing import Dict

# Base paths
RAG_DIR = os.path.dirname(os.path.abspath(__file__))

# Embedding model configuration
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

# Database paths and metadata
DB_PATHS: Dict[str, Dict[str, str]] = {
    'primevue': {
        'path': os.path.join(RAG_DIR, 'chroma_db_primevue'),
        'name': 'PrimeVue',
        'source_file': os.path.join(RAG_DIR, 'primevue-llms-full.txt')
    },
    'nuxt': {
        'path': os.path.join(RAG_DIR, 'chroma_db_nuxt'),
        'name': 'Nuxt',
        'source_file': os.path.join(RAG_DIR, 'nuxt-llms-full.txt')
    }
}

# Chunking configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval configuration
TOP_K = 7  # Number of fragments to retrieve per database
BATCH_SIZE = 100  # Batch size for indexing

# Markdown header configuration
HEADERS_TO_SPLIT_ON = [
    ("#", "Header_1"),
    ("##", "Header_2"),
    ("###", "Header_3"),
]
