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
│   └── copilot-instructions.md    # Instrukcje dla GitHub Copilot
├── .vscode/
│   ├── settings.json              # Konfiguracja VSCode
│   ├── extensions.json            # Rekomendowane rozszerzenia
│   └── launch.json                # Konfiguracja debugowania
├── RAG/
│   ├── index_db.py                # Skrypt indeksowania
│   ├── nuxt-llms-full.txt         # Dokumentacja Nuxt (2.8MB)
│   ├── primevue-llms-full.txt     # Dokumentacja PrimeVue (1.8MB)
│   ├── chroma_db_nuxt/            # Baza wektorowa Nuxt (37MB)
│   ├── chroma_db_primevue/        # Baza wektorowa PrimeVue (24MB)
│   ├── requirements.txt           # Zależności Python
│   └── README.md                  # Szczegółowa dokumentacja RAG
├── .gitignore
└── README.md                      # Ten plik
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

## 📊 Status projektu

- ✅ Indeksowanie dokumentacji Nuxt
- ✅ Indeksowanie dokumentacji PrimeVue
- ✅ Bazy wektorowe ChromaDB
- ⏳ Skrypt zapytań (query_db.py)
- ⏳ FastAPI backend
- ⏳ Frontend Nuxt + PrimeVue
- ⏳ Integracja z LLM (GPT-4/Claude)

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
