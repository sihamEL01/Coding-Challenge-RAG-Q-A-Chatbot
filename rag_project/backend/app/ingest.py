# backend/app/ingest.py
from documents import extract_text_from_pdf, chunk_text
from embeddings import embed_texts
from vector_store import save_documents

pdf_path = "D:/quorium project/rag_project/Schatzinsel_E.pdf"  # replace with your PDF

# 1. Extract text
text = extract_text_from_pdf(pdf_path)

# 2. Chunk text
chunks = chunk_text(text)

# 3. Generate embeddings
embeddings = embed_texts(chunks)

# 4. Save to FAISS
save_documents(
    embeddings=embeddings,
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)


print(f"Ingested {len(chunks)} chunks and saved FAISS index.")
