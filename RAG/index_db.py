import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# KONFIGURACJA
FILE_PATH = "nuxt-llms-full.txt"
DB_PATH = "./chroma_db_nuxt"

def build_index():
    print(f"1. 📖 Wczytywanie {FILE_PATH}...")
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # --- STRATEGIA CHUNKOWANIA DLA MNIEJSZYCH HALUCYNACJI ---
    # Krok A: Dzielimy logicznie po nagłówkach Markdown (żeby zachować kontekst sekcji)
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    md_header_splits = markdown_splitter.split_text(text)

    print(f"   Znaleziono {len(md_header_splits)} logicznych sekcji Markdown.")

    # Krok B: Docinamy zbyt długie sekcje, ale zachowujemy metadane nagłówków
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    final_splits = text_splitter.split_documents(md_header_splits)
    print(f"   Podzielono na {len(final_splits)} ostatecznych chunków (z kontekstem nagłówków).")

    # --- EMBEDDING ---
    print("2. 🧠 Tworzenie embeddingów (może to chwilę potrwać)...")
    # Używamy lokalnego modelu (darmowy, szybki, dobry do kodu)
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Zapis do ChromaDB
    Chroma.from_documents(
        documents=final_splits,
        embedding=embedding_function,
        persist_directory=DB_PATH
    )
    print(f"✅ Sukces! Baza zapisana w {DB_PATH}")

if __name__ == "__main__":
    build_index()