# 🤖 RAG System - Nuxt & PrimeVue Documentation Assistant

System RAG (Retrieval-Augmented Generation) do inteligentnego wyszukiwania i odpowiadania na pytania dotyczące dokumentacji Nuxt.js i PrimeVue.

## 📌 O projekcie

Ten projekt wykorzystuje bazę wektorową ChromaDB i model embedujący Sentence Transformers do:

- Indeksowania pełnej dokumentacji Nuxt.js i PrimeVue
- Semantycznego wyszukiwania odpowiednich fragmentów
- Przygotowania kontekstu dla LLM do generowania odpowiedzi

## 🚀 Quick Start

```bash
# 1. Instalacja zależności systemowych
sudo apt install python3-pip python3-venv

# 2. Instalacja bibliotek Python
pip install -r RAG/requirements.txt

# 3. Indeksowanie dokumentacji (już wykonane)
cd RAG
python3 index_db.py
```

## 📁 Struktura projektu

```
nuxt-primevue-rag/
├── .github/
│   └── copilot-instructions.md      # Instrukcje dla GitHub Copilot
├── .vscode/
│   ├── settings.json                # Konfiguracja VSCode
│   ├── extensions.json              # Rekomendowane rozszerzenia
│   ├── launch.json                  # Konfiguracja debugowania
│   ├── tasks.json                   # ⭐ Tasks dla VSCode
│   └── keybindings.json             # ⭐ Skróty klawiszowe
├── .vscode-extension/               # ⭐ VSCode Extension
│   ├── package.json
│   ├── extension.js
│   ├── README.md
│   └── .vscodeignore
├── RAG/
│   ├── index_db.py                  # Skrypt indeksowania
│   ├── generate_prompt.py           # Generator promptów (PrimeVue)
│   ├── generate_prompt_universal.py # Generator promptów (Universal)
│   ├── quick_query.py               # ⭐ Python CLI wrapper
│   ├── USAGE.md                     # ⭐ Przewodnik użycia z Copilot
│   ├── QUICKSTART.md                # Quick start guide
│   ├── EXAMPLE_QUESTIONS.md         # 50+ przykładowych pytań
│   ├── nuxt-llms-full.txt           # Dokumentacja Nuxt (2.8MB)
│   ├── primevue-llms-full.txt       # Dokumentacja PrimeVue (1.8MB)
│   ├── chroma_db_nuxt/              # Baza wektorowa Nuxt (37MB)
│   ├── chroma_db_primevue/          # Baza wektorowa PrimeVue (24MB)
│   ├── requirements.txt             # Zależności Python
│   └── README.md                    # Szczegółowa dokumentacja RAG
├── AUTOMATION.md                    # ⭐ Przewodnik automatyzacji
├── .gitignore
└── README.md                        # Ten plik
```

## 🛠️ Stack technologiczny

### Backend

- **Python 3.10+**
- **LangChain** - framework do aplikacji LLM
- **ChromaDB** - baza wektorowa
- **Sentence Transformers** - model `all-MiniLM-L6-v2`

### Frontend (planowany)

- **Nuxt 3** - Vue.js framework
- **PrimeVue** - UI component library
- **TypeScript**

## 🎯 ZERO HALUCYNACJI - Użycie z GitHub Copilot

### 🚀 3 Sposoby automatyzacji workflow

#### 🥇 Metoda 1: VSCode Extension (NAJLEPSZY DX!)

**One-click RAG queries bezpośrednio w VSCode!**

```bash
cd .vscode-extension
npm install
vsce package
code --install-extension rag-copilot-helper-1.0.0.vsix
```

**Użycie:** Naciśnij `Ctrl+Shift+R` → Wpisz pytanie → Gotowe! 🎉

📖 [Instrukcje instalacji extension](.vscode-extension/README.md)

#### 🥈 Metoda 2: VSCode Tasks + Keybindings

**Skonfigurowane i gotowe do użycia!**

- `Ctrl+Shift+R Q` - Quick Query
- `Ctrl+Shift+R P` - Query PrimeVue
- `Ctrl+Shift+R N` - Query Nuxt
- `Ctrl+Shift+R B` - Query Both

#### 🥉 Metoda 3: Python CLI

```bash
cd RAG
python3 quick_query.py "Your question" --db both --copy
```

🎬 **Kompletny przewodnik automatyzacji:** [AUTOMATION.md](AUTOMATION.md)
📖 **Pełny przewodnik użycia:** [RAG/USAGE.md](RAG/USAGE.md)
💡 **50+ Przykładowych pytań:** [RAG/EXAMPLE_QUESTIONS.md](RAG/EXAMPLE_QUESTIONS.md)

### Jak to działa?

1. Zadajesz pytanie (np. "Jak zrobić DataTable w PrimeVue?")
2. Skrypt przeszukuje bazę wektorową i znajduje 7 najbardziej relevantnych fragmentów dokumentacji
3. Generuje gotowy prompt z kontekstem i regułami anty-halucynacyjnymi
4. Kopiujesz prompt i wklejasz do GitHub Copilot Chat w VS Code
5. Copilot odpowiada **TYLKO** na podstawie dostarczonych fragmentów dokumentacji

**Rezultat:** Precyzyjny kod bez wymyślania, ze źródłami z dokumentacji. ✅

---

## 📊 Status projektu

### ✅ Gotowe (Production Ready!)

- ✅ Indeksowanie dokumentacji Nuxt
- ✅ Indeksowanie dokumentacji PrimeVue
- ✅ Bazy wektorowe ChromaDB (61MB łącznie)
- ✅ **Generator promptów dla Copilot (generate_prompt.py)**
- ✅ **Universal query tool (generate_prompt_universal.py)**
- ✅ **Python CLI wrapper (quick_query.py)**
- ✅ **VSCode Extension (rag-copilot-helper)**
- ✅ **VSCode Tasks + Keybindings**
- ✅ **Kompletna dokumentacja (USAGE.md, AUTOMATION.md)**
- ✅ **50+ przykładowych pytań (EXAMPLE_QUESTIONS.md)**

### ⏳ Planowane rozszerzenia

- ⏳ FastAPI backend z /api/query endpoint
- ⏳ Frontend Nuxt + PrimeVue z chat interface
- ⏳ Bezpośrednia integracja LLM (OpenAI/Anthropic)
- ⏳ Docker deployment

## 🔍 Jak to działa?

1. **Chunking** - Dokumenty są dzielone na mniejsze fragmenty (1000 znaków)
2. **Embedding** - Każdy fragment jest zamieniany na wektor 384-wymiarowy
3. **Indexing** - Wektory są zapisywane w ChromaDB
4. **Retrieval** - Zapytanie użytkownika jest wektoryzowane i wyszukiwane są najbardziej podobne fragmenty
5. **Generation** - LLM generuje odpowiedź na podstawie znalezionych fragmentów

## 📚 Więcej informacji

- Szczegółowa dokumentacja: [RAG/README.md](RAG/README.md)
- Instrukcje dla Copilot: [.github/copilot-instructions.md](.github/copilot-instructions.md)

## 🤝 Contributing

Projekt edukacyjny - do użytku własnego.

## 📄 Licencja

MIT - do użytku edukacyjnego i osobistego.
