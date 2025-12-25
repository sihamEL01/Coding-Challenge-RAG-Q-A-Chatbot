# backend/app/main.py
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .embeddings import embed_texts
from .vector_store import query_documents
from .llm import generate_answer

app = FastAPI(title="RAG Q&A")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str
    top_k: int = 5


@app.post("/ask")
def ask_question(req: QuestionRequest):
    question = req.question
    top_k = req.top_k

    # 1️⃣ Embed the question
    query_embedding = embed_texts([question])[0]

    # 2️⃣ Retrieve relevant chunks from ChromaDB
    results = query_documents(
        query_embedding=query_embedding,
        top_k=top_k
    )

    retrieved_chunks = results["documents"][0]
    retrieved_ids = results["ids"][0]

    # 3️⃣ Assemble context
    context = "\n\n".join(retrieved_chunks)

    # 4️⃣ Generate answer with LLM
    final_answer = generate_answer(question, context)

    return {
    "answer": final_answer,
    "sources": retrieved_chunks
}

