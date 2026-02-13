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
├── index_db.py              # Skrypt do indeksowania dokumentów
├── nuxt-llms-full.txt       # Dokumentacja Nuxt
├── primevue-llms-full.txt   # Dokumentacja PrimeVue
├── chroma_db_nuxt/          # Baza wektorowa Nuxt (37MB)
├── chroma_db_primevue/      # Baza wektorowa PrimeVue (24MB)
└── README.md                # Ten plik
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

## 📖 Przykład zapytania (TODO)

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

1. **Utworzenie skryptu zapytań** - `query_db.py` do testowania wyszukiwania
2. **Backend API** - FastAPI do obsługi zapytań z frontendu
3. **Frontend Nuxt** - interfejs użytkownika z PrimeVue
4. **Integracja z LLM** - dodanie GPT/Claude do generowania odpowiedzi

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
