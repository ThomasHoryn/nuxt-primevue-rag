# 🤖 RAG System - Nuxt & PrimeVue Documentation Assistant

RAG (Retrieval-Augmented Generation) system for intelligent search and question answering about Nuxt.js and PrimeVue documentation.

## 📌 About the project

This project uses ChromaDB vector database and Sentence Transformers embedding model to:

- Index complete Nuxt.js and PrimeVue documentation
- Semantic search for relevant fragments
- Prepare context for LLM to generate responses

## 🚀 Quick Start

```bash
# 1. Install system dependencies
sudo apt install python3-pip python3-venv

# 2. Install Python libraries
pip install -r RAG/requirements.txt

# 3. Index documentation (already done)
cd RAG
python3 index_db.py
```

## 📁 Project structure

```
nuxt-primevue-rag/
├── .github/
│   └── copilot-instructions.md      # Instructions for GitHub Copilot
├── .vscode/
│   ├── settings.json                # VSCode configuration
│   ├── extensions.json              # Recommended extensions
│   ├── launch.json                  # Debug configuration
│   ├── tasks.json                   # ⭐ VSCode Tasks
│   └── keybindings.json             # ⭐ Keyboard shortcuts
├── .vscode-extension/               # ⭐ VSCode Extension
│   ├── package.json
│   ├── extension.js
│   ├── README.md
│   └── .vscodeignore
├── RAG/
│   ├── index_db.py                  # Indexing script
│   ├── generate_prompt.py           # Prompt generator (PrimeVue)
│   ├── generate_prompt_universal.py # Prompt generator (Universal)
│   ├── quick_query.py               # ⭐ Python CLI wrapper
│   ├── USAGE.md                     # ⭐ Usage guide with Copilot
│   ├── QUICKSTART.md                # Quick start guide
│   ├── EXAMPLE_QUESTIONS.md         # 50+ example questions
│   ├── nuxt-llms-full.txt           # Nuxt documentation (2.8MB)
│   ├── primevue-llms-full.txt       # PrimeVue documentation (1.8MB)
│   ├── chroma_db_nuxt/              # Nuxt vector database (37MB)
│   ├── chroma_db_primevue/          # PrimeVue vector database (24MB)
│   ├── requirements.txt             # Python dependencies
│   └── README.md                    # Detailed RAG documentation
├── AUTOMATION.md                    # ⭐ Automation guide
├── .gitignore
└── README.md                        # This file
```

## 🛠️ Tech stack

### Backend

- **Python 3.10+**
- **LangChain** - framework do aplikacji LLM
- **ChromaDB** - baza wektorowa
- **Sentence Transformers** - model `all-MiniLM-L6-v2`

### Frontend (planned)

- **Nuxt 3** - Vue.js framework
- **PrimeVue** - UI component library
- **TypeScript**

## 🎯 ZERO HALLUCINATION - Usage with GitHub Copilot

### 🚀 3 Ways to automate workflow

#### 🥇 Method 1: VSCode Extension (BEST DX!)

**One-click RAG queries directly in VSCode!**

```bash
cd .vscode-extension
npm install
vsce package
code --install-extension rag-copilot-helper-1.0.0.vsix
```

**Usage:** Press `Ctrl+Shift+R` → Type your question → Done! 🎉

📖 [Extension installation guide](.vscode-extension/README.md)

#### 🥈 Method 2: VSCode Tasks + Keybindings

**Configured and ready to use!**

- `Ctrl+Shift+R Q` - Quick Query
- `Ctrl+Shift+R P` - Query PrimeVue
- `Ctrl+Shift+R N` - Query Nuxt
- `Ctrl+Shift+R B` - Query Both

#### 🥉 Method 3: Python CLI

```bash
cd RAG
python3 quick_query.py "Your question" --db both --copy
```

🎬 **Complete automation guide:** [AUTOMATION.md](AUTOMATION.md)
📖 **Full usage guide:** [RAG/USAGE.md](RAG/USAGE.md)
💡 **50+ Example questions:** [RAG/EXAMPLE_QUESTIONS.md](RAG/EXAMPLE_QUESTIONS.md)

### How it works?

1. You ask a question (e.g. "How to create a DataTable in PrimeVue?")
2. The script searches the vector database and finds the 7 most relevant documentation fragments
3. Generates a ready-made prompt with context and anti-hallucination rules
4. You copy the prompt and paste it into GitHub Copilot Chat in VS Code
5. Copilot responds **ONLY** based on the provided documentation fragments

**Result:** Precise code without guessing, with sources from documentation. ✅

---

## 📊 Project status

### ✅ Ready (Production Ready!)

- ✅ Nuxt documentation indexing
- ✅ PrimeVue documentation indexing
- ✅ ChromaDB vector databases (61MB total)
- ✅ **Prompt generator for Copilot (generate_prompt.py)**
- ✅ **Universal query tool (generate_prompt_universal.py)**
- ✅ **Python CLI wrapper (quick_query.py)**
- ✅ **VSCode Extension (rag-copilot-helper)**
- ✅ **VSCode Tasks + Keybindings**
- ✅ **Complete documentation (USAGE.md, AUTOMATION.md)**
- ✅ **50+ example questions (EXAMPLE_QUESTIONS.md)**

### ⏳ Planned extensions

- ⏳ FastAPI backend with /api/query endpoint
- ⏳ Nuxt + PrimeVue frontend with chat interface
- ⏳ Direct LLM integration (OpenAI/Anthropic)
- ⏳ Docker deployment

## 🔍 How it works?

1. **Chunking** - Documents are split into smaller fragments (1000 characters)
2. **Embedding** - Each fragment is converted to a 384-dimensional vector
3. **Indexing** - Vectors are stored in ChromaDB
4. **Retrieval** - User query is vectorized and most similar fragments are found
5. **Generation** - LLM generates response based on retrieved fragments

## 📚 More information

- Detailed documentation: [RAG/README.md](RAG/README.md)
- Instructions for Copilot: [.github/copilot-instructions.md](.github/copilot-instructions.md)

## 🤝 Contributing

Educational project - for personal use.

## 📄 License

MIT - for educational and personal use.
