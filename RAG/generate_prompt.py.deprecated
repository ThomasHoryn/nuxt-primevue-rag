import os
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# --- KONFIGURACJA ---
DB_PATH = "./chroma_db_primevue"
TOP_K = 7  # Ile fragmentów dokumentacji pobrać (dla Claude Sonnet możesz dać więcej, np. 7-10)

def main():
    # 1. Ładowanie bazy (bez API key)
    if not os.path.exists(DB_PATH):
        print(f"❌ Błąd: Nie znaleziono bazy w {DB_PATH}. Uruchom najpierw index_db.py")
        return

    print("🧠 Ładowanie bazy wektorowej (tryb offline)...")
    # Ten sam model embedujący co przy indeksowaniu
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embedding_function)

    print(f"\n✅ Gotowe. Wpisz pytanie, a ja przygotuję prompt do wklejenia (Ctrl+C by wyjść).")

    while True:
        question = input("\n🔎 O co chcesz zapytać?: ")
        if not question.strip(): continue
        if question.lower() in ['exit', 'quit']: break

        # 2. Wyszukiwanie (Retrieval)
        print("...Szukam najlepszych fragmentów w dokumentacji...")
        docs = vectorstore.similarity_search(question, k=TOP_K)

        # 3. Budowanie kontekstu
        context_str = ""
        for i, doc in enumerate(docs):
            # Wyciągamy nagłówki Markdown, żeby wiedzieć co to za sekcja
            header = f"{doc.metadata.get('Header 1', '')} > {doc.metadata.get('Header 2', '')}"
            content = doc.page_content
            context_str += f"--- FRAGMENT {i+1} (Źródło: {header}) ---\n{content}\n\n"

        # 4. Składanie finalnego promptu (System + Context + Question)
        final_output = f"""
================ SKOPIUJ PONIŻEJ ================

You are an expert coding assistant for PrimeVue.
Answer SOLELY based on the provided context.

<critical_rules>
1. **NO OUTSIDE KNOWLEDGE**: If the answer is not in <context>, say: "Brak informacji w dokumentacji."
2. **CITATION MANDATORY**: Cite source headers for every code block.
3. **COMPOSITION API**: Use <script setup>.
</critical_rules>

<context>
{context_str}
</context>

User Question: {question}

================ KONIEC KOPIOWANIA ================
"""
        print(final_output)
        print("💡 Wskazówka: Zaznacz tekst między liniami i wklej do Claude/Copilot.")

if __name__ == "__main__":
    main()
