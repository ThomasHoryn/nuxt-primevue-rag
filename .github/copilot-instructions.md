# GitHub Copilot Instructions - RAG System dla Nuxt & PrimeVue

## Kontekst projektu

To jest system RAG (Retrieval-Augmented Generation) do wyszukiwania informacji w dokumentacji Nuxt.js i PrimeVue przy użyciu bazy wektorowej ChromaDB.

## Stack technologiczny

### Backend (Python)

- **LangChain** - framework do budowy aplikacji LLM
- **ChromaDB** - baza wektorowa do przechowywania embeddingów
- **Sentence Transformers** - model `all-MiniLM-L6-v2` do generowania embeddingów
- **FastAPI** (planowane) - API REST

### Frontend (planowany)

- **Nuxt 3** - framework Vue.js
- **PrimeVue** - biblioteka komponentów UI
- **TypeScript**

## Struktura projektu

```
nuxt-primevue-rag/
├── .github/
│   └── copilot-instructions.md
├── RAG/
│   ├── index_db.py              # Indeksowanie dokumentów
│   ├── nuxt-llms-full.txt       # Dokumentacja Nuxt
│   ├── primevue-llms-full.txt   # Dokumentacja PrimeVue
│   ├── chroma_db_nuxt/          # Baza wektorowa Nuxt
│   ├── chroma_db_primevue/      # Baza wektorowa PrimeVue
│   ├── requirements.txt
│   └── README.md
```

## Konwencje kodowania

### Python

- **Style**: PEP 8
- **Naming**: snake_case dla funkcji i zmiennych
- **Docstrings**: Google style
- **Type hints**: używaj wszędzie gdzie możliwe
- **Imports**: grupuj w kolejności: stdlib, third-party, local

### Przykład kodu Python:

```python
from typing import List, Dict
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

def retrieve_documents(query: str, k: int = 5) -> List[Dict]:
    """
    Wyszukuje najbardziej podobne dokumenty do zapytania.

    Args:
        query: Pytanie użytkownika
        k: Liczba dokumentów do zwrócenia

    Returns:
        Lista dokumentów z metadanymi
    """
    pass
```

### TypeScript/Vue (gdy będzie frontend)

- **Style**: Standard Vue 3 + Composition API
- **Naming**: camelCase dla zmiennych, PascalCase dla komponentów
- **Components**: Single File Components (.vue)
- **Composables**: prefix `use` (np. `useRAGQuery`)

## Kluczowe parametry projektu

### Chunking dokumentów

```python
chunk_size = 1000        # Rozmiar fragmentu tekstu
chunk_overlap = 200      # Nakładanie między fragmentami
```

### Wyszukiwanie

```python
k = 5                    # Liczba zwracanych dokumentów
model = "all-MiniLM-L6-v2"  # Model embeddingowy
```

## Wskazówki dla Copilot

1. **Obsługa błędów**: Zawsze dodawaj try-except dla operacji I/O i połączeń z bazą
2. **Logowanie**: Używaj emoji w printach dla lepszej czytelności (📖, 🧠, ✅, ❌)
3. **Komentarze**: Używaj polskich komentarzy dla spójności z resztą kodu
4. **Embeddingi**: Pamiętaj o cache'owaniu modelu embeddingowego
5. **Chunking**: Zawsze zachowuj kontekst nagłówków Markdown
6. **Metadane**: Dodawaj źródło dokumentu (nuxt/primevue) do każdego fragmentu

## Planowane funkcjonalności

- [ ] Skrypt query_db.py do testowania zapytań
- [ ] FastAPI backend z endpointem /api/query
- [ ] Połączenie obu baz w jeden system
- [ ] Frontend w Nuxt 3 z interfejsem czatu
- [ ] Integracja z LLM (OpenAI/Anthropic) dla generowania odpowiedzi
- [ ] System cache'owania często zadawanych pytań
- [ ] Deployment (Docker)

## Przykładowe zapytania do systemu RAG

- "Jak używać composables w Nuxt 3?"
- "Jak skonfigurować DataTable w PrimeVue?"
- "Jaka jest różnica między pages i components w Nuxt?"
- "Jak stylować komponenty PrimeVue?"

## Dane źródłowe

- `nuxt-llms-full.txt` - 2.8 MB - pełna dokumentacja Nuxt
- `primevue-llms-full.txt` - 1.8 MB - pełna dokumentacja PrimeVue

Dokumenty są w formacie Markdown z nagłówkami strukturyzującymi treść.

## Uwagi dotyczące wydajności

- Model embeddingowy (~90MB) jest cache'owany po pierwszym użyciu
- Pierwsza indeksacja może trwać 1-2 minuty
- Zapytania do bazy są szybkie (~100-200ms)
- Baza wektorowa zajmuje łącznie ~61MB
