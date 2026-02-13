# GitHub Copilot Instructions - RAG System for Nuxt & PrimeVue

## Project Context

This is a RAG (Retrieval-Augmented Generation) system for searching information in Nuxt.js and PrimeVue documentation using the ChromaDB vector database.

## Technology Stack

### Backend (Python)

- **LangChain** - framework for building LLM applications
- **ChromaDB** - vector database for storing embeddings
- **Sentence Transformers** - `all-MiniLM-L6-v2` model for generating embeddings
- **FastAPI** (planned) - REST API

### Frontend (planned)

- **Nuxt 3** - Vue.js framework
- **PrimeVue** - UI component library
- **TypeScript**

## Project Structure

```
nuxt-primevue-rag/
├── .github/
│   └── copilot-instructions.md
├── RAG/
│   ├── index_db.py              # Document indexing
│   ├── quick_query.py           # CLI query tool
│   ├── config.py                # Configuration
│   ├── QUICKSTART.md            # Quick start guide
│   ├── USAGE.md                 # Full usage documentation
│   ├── EXAMPLE_QUESTIONS.md     # Example questions
│   ├── nuxt-llms-full.txt       # Nuxt documentation
│   ├── primevue-llms-full.txt   # PrimeVue documentation
│   ├── chroma_db_nuxt/          # Nuxt vector database
│   ├── chroma_db_primevue/      # PrimeVue vector database
│   ├── requirements.txt
│   └── README.md
```

## 🎯 RAG-Copilot Workflow (ZERO HALLUCINATION)

### Philosophy

Instead of letting Copilot make up code, **you feed it documentation fragments** before each question.

### Workflow:

1. Run `python3 quick_query.py "Your question" --db both`
2. Ask question (e.g. "How to create DataTable in PrimeVue?")
3. Copy generated prompt (contains documentation fragments)
4. Paste to GitHub Copilot Chat in VS Code
5. Copilot responds ONLY based on provided fragments

### Critical Rules for prompts:

```
1. NO OUTSIDE KNOWLEDGE - use only context
2. CITATION MANDATORY - cite sources (Headers)
3. COMPOSITION API - use <script setup>
4. NO HALLUCINATION - zero API invention
```

### When using this system as Copilot:

- ✅ Analyze **only** fragments in `<context>`
- ✅ Cite sources: "Source: Header 1 > Header 2"
- ✅ Use code patterns exactly as in documentation
- ❌ DO NOT invent APIs that are not in context
- ❌ DO NOT use knowledge from outside provided fragments

## Coding Conventions

### Python

- **Style**: PEP 8
- **Naming**: snake_case for functions and variables
- **Docstrings**: Google style
- **Type hints**: use everywhere possible
- **Imports**: group in order: stdlib, third-party, local

### Python Code Example:

```python
from typing import List, Dict
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

def retrieve_documents(query: str, k: int = 5) -> List[Dict]:
    """
    Searches for documents most similar to the query.

    Args:
        query: User question
        k: Number of documents to return

    Returns:
        List of documents with metadata
    """
    pass
```

### TypeScript/Vue (when frontend is built)

- **Style**: Standard Vue 3 + Composition API
- **Naming**: camelCase for variables, PascalCase for components
- **Components**: Single File Components (.vue)
- **Composables**: prefix `use` (e.g. `useRAGQuery`)

## Key Project Parameters

### Document Chunking

```python
chunk_size = 1000        # Text fragment size
chunk_overlap = 200      # Overlap between fragments
```

### Search

```python
k = 7                    # Number of returned documents (configurable in config.py)
model = "all-MiniLM-L6-v2"  # Embedding model
```

## Guidelines for Copilot

1. **Error Handling**: Always add try-except for I/O operations and database connections
2. **Logging**: Use emojis in prints for better readability (📖, 🧠, ✅, ❌)
3. **Comments**: Use English comments for consistency
4. **Embeddings**: Remember to cache the embedding model
5. **Chunking**: Always preserve context of Markdown headers
6. **Metadata**: Add document source (nuxt/primevue) to each fragment

## Functionality Status

- [x] Documentation indexing (index_db.py)
- [x] Unified CLI tool (quick_query.py)
- [x] Configuration management (config.py)
- [x] VSCode Extension (rag-copilot-helper)
- [x] VSCode Tasks + Keybindings
- [x] Usage documentation (QUICKSTART.md, USAGE.md, EXAMPLE_QUESTIONS.md, AUTOMATION.md)
- [x] VSCode configuration for Copilot
- [ ] FastAPI backend with /api/query endpoint
- [ ] Nuxt 3 frontend with chat interface
- [ ] Caching system for frequently asked questions
- [ ] Deployment (Docker)

## 🚀 Automation Tools

### VSCode Extension (Recommended)

**Best DX:** One-click RAG queries directly in VS Code!

```bash
cd .vscode-extension
npm install
code --install-extension rag-copilot-helper-*.vsix
```

**Usage:** `Ctrl+Shift+R` → question → DONE!

### Python CLI

```bash
python3 RAG/quick_query.py "Your question" --db both --copy
```

### VSCode Tasks

- `Ctrl+Shift+R Q` - Quick Query
- `Ctrl+Shift+R P` - Query PrimeVue
- `Ctrl+Shift+R N` - Query Nuxt
- `Ctrl+Shift+R B` - Query Both

Full documentation: [AUTOMATION.md](../AUTOMATION.md)

## Example RAG System Queries

- "How to use composables in Nuxt 3?"
- "How to configure DataTable in PrimeVue?"
- "What is the difference between pages and components in Nuxt?"
- "How to style PrimeVue components?"

## Source Data

- `nuxt-llms-full.txt` - 2.8 MB - full Nuxt documentation
- `primevue-llms-full.txt` - 1.8 MB - full PrimeVue documentation

Documents are in Markdown format with headers structuring the content.

## Performance Notes

- Embedding model (~90MB) is cached after first use
- First indexing may take 1-2 minutes
- Database queries are fast (~100-200ms)
- Vector database takes ~61MB total
