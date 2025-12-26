# 📚 RAG Question Answering System – Quorium Coding Challenge

This project implements a **Retrieval-Augmented Generation (RAG)** system for question answering over documents, developed as part of the **Quorium AI Engineer Trainee Coding Challenge**.

The system ingests documents, indexes them using vector embeddings, retrieves the most relevant chunks for a user query, and generates answers **grounded strictly in the retrieved context**.

---

## 🚀 Features

- 📄 Supports document ingestion from **PDF, TXT, and Markdown**
- ✂️ Intelligent text chunking with overlap
- 🧠 Semantic search using **ChromaDB** vector store
- 🤖 LLM-based answer generation ("meta-llama/Meta-Llama-3-8B-Instruct")
- ⚡ FastAPI backend with clean REST endpoints
- 💬 Simple chat-style frontend (Next.js)
- 🐳 Docker-first setup for reproducibility

---

## 🧠 Architecture Overview

```

User Question
│
▼
[Embed Question]
│
▼
[ChromaDB Vector Search]
│
▼
[Top-K Relevant Chunks]
│
▼
[Context Construction]
│
▼
[LLM Answer Generation]

```

---

## 🏗️ Tech Stack

### Backend
- FastAPI  
- ChromaDB (Vector Store)  
- SentenceTransformers (`all-MiniLM-L6-v2`)  
- "meta-llama/Meta-Llama-3-8B-Instruct"  
- Python 3.13+

### Frontend
- Next.js  
- React  
- Minimal chat interface

### DevOps
- Docker & Docker Compose  
- Custom `docker.sh` wrapper

---

## 📦 Project Structure

```

rag_project/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app
│   │   ├── ingest.py        # Document ingestion
│   │   ├── embeddings.py   # Embedding logic
│   │   ├── vector_store.py # ChromaDB logic
│   │   ├── llm.py          # LLM interface
│   │   └── utils.py
│   └── Dockerfile
│
├── frontend/
│   ├── pages/
│   ├── components/
│   └── Dockerfile
│
├── docker-compose.yml
├── docker.sh
├── README.md

````

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/rag-quorium-challenge.git
cd rag-quorium-challenge
````

---


### 2️⃣ Build Docker images

```bash
./docker.sh build
```

---

###3️⃣ Start the system

```bash
./docker.sh up
```

Services will be available at:

* Backend API: `http://localhost:8000`
* Frontend: `http://localhost:3000`

---

## 📥 Document Ingestion

To ingest documents into the vector store:

```bash
./docker.sh ingest
```

This process:

* Parses documents (`.pdf`, `.txt`, `.md`)
* Cleans non-content sections
* Splits text into **300–500 token chunks**
* Generates embeddings
* Stores them in **ChromaDB**

---

## ❓ Question Answering API

### Endpoint

```http
POST /ask
```

### Request Body

```json
{
  "question": "Who gives Jim the black spot?",
  "top_k": 5
}
```

### Response

```json
{
  "answer": "Blind Pew gives Jim the black spot.",
  "sources": [
    "chunk_12",
    "chunk_15"
  ]
}
```

---

## 🛡️ Grounded Answering (No Hallucinations)

The language model is explicitly instructed to:

* Use **only the retrieved context**
* **Never guess or hallucinate**
* Return:

> *"I don't know based on the provided context."*

when the answer is not present.

This ensures factual and explainable answers.

---

## 🧪 Known Limitations

* Retrieval quality depends on chunking strategy
* Long narrative documents require careful overlap tuning
* LLM responses depend on external API availability

---

## 📈 Future Improvements

* Hybrid retrieval (BM25 + embeddings)
* Metadata-aware search (chapters, entities)
* Cross-encoder re-ranking
* Streaming responses
* Enhanced frontend UX


---

## 👤 Author

**Siham El Yaagoubi**
AI / Data Engineering Student
Quorium Coding Challenge – 2025

```
