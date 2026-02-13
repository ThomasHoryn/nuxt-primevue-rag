import os
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# --- KONFIGURACJA ---
DATABASES = {
    "1": {"path": "./chroma_db_primevue", "name": "PrimeVue"},
    "2": {"path": "./chroma_db_nuxt", "name": "Nuxt"},
}
TOP_K = 7  # Ile fragmentów dokumentacji pobrać

def main():
    print("🎯 Wybierz źródło dokumentacji:")
    print("1. PrimeVue")
    print("2. Nuxt")
    print("3. Oba (wyszukiwanie w obu bazach)")

    choice = input("\nWybór (1/2/3): ").strip()

    if choice not in ["1", "2", "3"]:
        print("❌ Nieprawidłowy wybór!")
        return

    # Sprawdzenie czy bazy istnieją
    if choice == "3":
        # Sprawdź obie bazy
        for key, db_info in DATABASES.items():
            if not os.path.exists(db_info["path"]):
                print(f"❌ Błąd: Nie znaleziono bazy {db_info['name']} w {db_info['path']}")
                return
    else:
        db_info = DATABASES[choice]
        if not os.path.exists(db_info["path"]):
            print(f"❌ Błąd: Nie znaleziono bazy {db_info['name']} w {db_info['path']}")
            return

    print("\n🧠 Ładowanie bazy wektorowej (tryb offline)...")
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Załaduj odpowiednie bazy
    vectorstores = {}
    if choice == "3":
        for key, db_info in DATABASES.items():
            vectorstores[db_info["name"]] = Chroma(
                persist_directory=db_info["path"],
                embedding_function=embedding_function
            )
    else:
        db_info = DATABASES[choice]
        vectorstores[db_info["name"]] = Chroma(
            persist_directory=db_info["path"],
            embedding_function=embedding_function
        )

    print(f"\n✅ Gotowe. Wpisz pytanie, a ja przygotuję prompt do wklejenia (Ctrl+C by wyjść).")

    while True:
        question = input("\n🔎 O co chcesz zapytać?: ")
        if not question.strip():
            continue
        if question.lower() in ['exit', 'quit']:
            break

        # 2. Wyszukiwanie w wybranych bazach
        print("...Szukam najlepszych fragmentów w dokumentacji...")
        all_docs = []

        for source_name, vectorstore in vectorstores.items():
            docs = vectorstore.similarity_search(question, k=TOP_K)
            # Dodaj źródło do metadanych
            for doc in docs:
                doc.metadata['source_db'] = source_name
                all_docs.append(doc)

        # Jeśli mamy obie bazy, posortuj wyniki
        if len(vectorstores) > 1:
            # Możemy tutaj posortować po relevance score jeśli byłby dostępny
            # Na razie tylko miesamy wyniki z obu baz
            all_docs = all_docs[:TOP_K * 2]  # Weź więcej fragmentów z obu baz

        # 3. Budowanie kontekstu
        context_str = ""
        for i, doc in enumerate(all_docs):
            source_db = doc.metadata.get('source_db', 'Unknown')
            header = f"{doc.metadata.get('Header 1', '')} > {doc.metadata.get('Header 2', '')}"
            content = doc.page_content
            context_str += f"--- FRAGMENT {i+1} (Źródło: {source_db} - {header}) ---\n{content}\n\n"

        # Określ framework dla promptu
        if len(vectorstores) == 1:
            framework = list(vectorstores.keys())[0]
        else:
            framework = "Nuxt and PrimeVue"

        # 4. Składanie finalnego promptu
        final_output = f"""
================ SKOPIUJ PONIŻEJ ================

You are an expert coding assistant for {framework}.
Answer SOLELY based on the provided context.

<critical_rules>
1. **NO OUTSIDE KNOWLEDGE**: If the answer is not in <context>, say: "Brak informacji w dokumentacji."
2. **CITATION MANDATORY**: Cite source headers for every code block.
3. **COMPOSITION API**: Use <script setup> for Vue/Nuxt components.
4. **NO HALLUCINATION**: Use ONLY patterns, APIs, and code shown in the context.
</critical_rules>

<context>
{context_str}
</context>

User Question: {question}

================ KONIEC KOPIOWANIA ================
"""
        print(final_output)
        print("💡 Wskazówka: Zaznacz tekst między liniami i wklej do GitHub Copilot Chat w VS Code.")
        print("   (Wyślij jako wiadomość w Copilot Chat - nie w edytorze)")

if __name__ == "__main__":
    main()
