# RAG System dla dokumentacji Nuxt i PrimeVue

System RAG (Retrieval-Augmented Generation) do wyszukiwania informacji w dokumentacji Nuxt.js i PrimeVue przy użyciu bazy wektorowej ChromaDB.

## 📋 Wymagania

- Python 3.10 lub nowszy
- pip (menedżer pakietów Python)
- Minimum 2GB wolnego miejsca na dysku (dla modeli embeddingowych)

## 🚀 Instalacja

### 1. Instalacja narzędzi systemowych (jeśli nie masz pip)

```bash
sudo apt install python3-pip python3-venv
```

### 2. Instalacja bibliotek Python

```bash
pip install langchain langchain-community langchain-chroma langchain-text-splitters sentence-transformers chromadb torch transformers pillow
```

lub możesz zainstalować z pliku requirements.txt:

```bash
pip install -r requirements.txt
```

## 📚 Struktura projektu

```
RAG/
├── index_db.py                      # Skrypt do indeksowania dokumentów
├── generate_prompt.py               # Generator promptów (PrimeVue)
├── generate_prompt_universal.py     # Generator promptów (Universal)
├── quick_query.py                   # 🆕 Python CLI wrapper
├── USAGE.md                         # 📖 Pełna dokumentacja użycia
├── QUICKSTART.md                    # 🚀 Quick start guide
├── EXAMPLE_QUESTIONS.md             # 💡 50+ przykładowych pytań
├── nuxt-llms-full.txt               # Dokumentacja Nuxt (2.8MB)
├── primevue-llms-full.txt           # Dokumentacja PrimeVue (1.8MB)
├── chroma_db_nuxt/                  # Baza wektorowa Nuxt (37MB)
├── chroma_db_primevue/              # Baza wektorowa PrimeVue (24MB)
├── requirements.txt                 # Zależności Python
└── README.md                        # Ten plik
```

## 🔧 Użycie

### Indeksowanie dokumentów

Skrypt `index_db.py` przetwarza pliki tekstowe i tworzy bazy wektorowe.

**Konfiguracja** - edytuj te zmienne w pliku `index_db.py`:

```python
FILE_PATH = "nuxt-llms-full.txt"      # Plik źródłowy
DB_PATH = "./chroma_db_nuxt"           # Lokalizacja bazy wektorowej
```

**Uruchomienie:**

```bash
cd RAG
python3 index_db.py
```

**Co się dzieje podczas indeksowania:**

1. Wczytanie pliku tekstowego
2. Podział na logiczne sekcje (według nagłówków Markdown)
3. Podział długich sekcji na mniejsze chunki (1000 znaków z nakładaniem 200)
4. Generowanie embeddingów za pomocą modelu `all-MiniLM-L6-v2`
5. Zapis do bazy wektorowej ChromaDB

**Pierwsze uruchomienie:**

- Model embedujący (~90MB) zostanie automatycznie pobrany z HuggingFace
- Proces może potrwać 1-2 minuty dla każdego pliku

### Wykonane bazy wektorowe

✅ **PrimeVue**: `chroma_db_primevue/` (24 MB)
✅ **Nuxt**: `chroma_db_nuxt/` (37 MB)

## 📖 Użycie RAG systemu

### 🆕 Metoda 1: Python CLI (quick_query.py)

**Najszybsza** - Jeden wiersz terminala!

```bash
python3 quick_query.py "How to use DataTable?" --db primevue
python3 quick_query.py "useState in Nuxt 3" --db nuxt
python3 quick_query.py "useFetch with DataTable" --db both

# Z auto-kopiowaniem do schowka
python3 quick_query.py "Your question" --db both --copy
```

**Parametry:**

- `question` - Twoje pytanie (wymagane)
- `--db` - Źródło: `primevue`, `nuxt`, `both` (default: `both`)
- `--copy` - Auto-kopiuj do schowka (wymaga `xclip` lub `xsel`)

### Metoda 2: Interactive (generate_prompt_universal.py)

```bash
python3 generate_prompt_universal.py

# Wybierz bazę (1=PrimeVue, 2=Nuxt, 3=Both)
# Zadaj pytanie
# Skopiuj prompt między liniami ====
```

### Metoda 3: VSCode Extension (Recommended dla DX!)

Zobacz [AUTOMATION.md](../AUTOMATION.md) dla instrukcji instalacji VSCode Extension.

**Usage:** `Ctrl+Shift+R` → pytanie → DONE! 🎉

---

### 📖 Dokumentacja

- **[AUTOMATION.md](../AUTOMATION.md)** - 3 sposoby automatyzacji workflow
- **[USAGE.md](USAGE.md)** - Pełny przewodnik użycia z GitHub Copilot
- **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide dla początkujących
- **[EXAMPLE_QUESTIONS.md](EXAMPLE_QUESTIONS.md)** - 50+ gotowych pytań testowych

---

## 📖 Przykład zapytania (Programmatic)

```python
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Załaduj bazę
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="./chroma_db_nuxt", embedding_function=embedding_function)

# Wyszukaj dokumenty
results = db.similarity_search("Jak używać composables w Nuxt?", k=3)

for doc in results:
    print(doc.page_content)
    print("---")
```

## 🛠️ Technologie

- **LangChain** - framework do budowy aplikacji LLM
- **ChromaDB** - baza wektorowa
- **Sentence Transformers** - generowanie embeddingów
- **all-MiniLM-L6-v2** - lekki model embedujący (384 wymiary)

## ⚙️ Parametry konfiguracyjne

### Chunking

```python
chunk_size=1000        # Rozmiar pojedynczego fragmentu tekstu
chunk_overlap=200      # Nakładanie między fragmentami (dla kontekstu)
```

### Wyszukiwanie

```python
k=3                    # Liczba zwracanych najbardziej podobnych dokumentów
```

## 📝 Kolejne kroki

1. ✅ **Skrypt zapytań** - `generate_prompt_universal.py`, `quick_query.py`
2. ✅ **VSCode Extension** - `rag-copilot-helper` dla maksymalnego DX
3. ✅ **VSCode Tasks + Keybindings** - `.vscode/tasks.json`, `.vscode/keybindings.json`
4. ✅ **Kompletna dokumentacja** - USAGE.md, AUTOMATION.md, EXAMPLE_QUESTIONS.md
5. ⏳ **Backend API** - FastAPI do obsługi zapytań z frontendu
6. ⏳ **Frontend Nuxt** - interfejs użytkownika z PrimeVue
7. ⏳ **Integracja z LLM** - dodanie GPT/Claude do generowania odpowiedzi bezpośrednio

## ❓ Troubleshooting

### ModuleNotFoundError: No module named 'langchain_community'

```bash
pip install --upgrade langchain-community
```

### Błąd PIL.Image.Resampling

```bash
pip install --upgrade pillow
```

### Brak modułu sentence_transformers

```bash
pip install --upgrade sentence-transformers transformers torch
```

## 📄 Licencja

Projekt edukacyjny - do użytku własnego.
