# RepoMind

> An AI-powered GitHub Repository & Documentation Assistant built with FastAPI, LangChain, Gemini, and Qdrant.

RepoMind is a Retrieval-Augmented Generation (RAG) application that allows users to upload documentation and source code repositories, semantically index them, and ask natural language questions about their contents.

Instead of keyword search, RepoMind understands the semantic meaning of both documents and code, making it easier to explore architectures, APIs, and implementation details.

---

# Features

## Current

* Upload documents
* Automatic document parsing
* Intelligent document chunking
* Google Gemini embeddings
* Semantic vector search using Qdrant
* Context-aware question answering
* FastAPI backend
* Modular project architecture

## Planned

* GitHub repository ingestion
* Recursive repository indexing
* Hybrid Search (BM25 + Vector Search)
* Cross-encoder reranking
* Conversation memory
* Streaming responses
* Multiple knowledge bases
* User authentication
* Document management
* Docker deployment
* Evaluation dashboard
* REST API documentation

---

# Tech Stack

## Backend

* FastAPI
* Pydantic
* Python

## LLM

* Google Gemini 2.5 Flash
* Gemini Embedding Model

## Retrieval

* LangChain
* Qdrant Vector Database

## Document Processing

* Docling
* Recursive Character Text Splitter

---

# Architecture

```text
                 Upload Document
                        │
                        ▼
              Save Temporary File
                        │
                        ▼
                 Parse Document
                        │
                        ▼
                  Chunk Document
                        │
                        ▼
              Generate Embeddings
                        │
                        ▼
              Store in Qdrant DB
                        │
                        ▼
                 User Question
                        │
                        ▼
             Generate Query Vector
                        │
                        ▼
            Semantic Vector Search
                        │
                        ▼
              Retrieve Top Chunks
                        │
                        ▼
               Build System Prompt
                        │
                        ▼
                 Gemini 2.5 Flash
                        │
                        ▼
                    Final Answer
```

---

# Project Structure

```text
src/
│
├── api/
│
├── chat/
│   ├── router.py
│   ├── schemas.py
│   ├── prompts.py
│   └── service.py
│
├── documents/
│   ├── router.py
│   ├── parser.py
│   ├── chunker.py
│   ├── service.py
│   └── utils.py
│
├── embeddings/
│   └── service.py
│
├── llm/
│   └── base.py
│
├── vectorstore/
│   ├── client.py
│   └── service.py
│
├── config.py
└── main.py
```

---

# How It Works

## Document Upload

1. User uploads a document.
2. The document is temporarily stored.
3. Docling parses the document.
4. The parsed content is split into chunks.
5. Gemini generates embeddings for every chunk.
6. Chunks and metadata are stored inside Qdrant.

---

## Question Answering

1. User submits a question.
2. The question is converted into an embedding.
3. Qdrant retrieves the most relevant chunks.
4. Retrieved chunks become the context.
5. Gemini generates an answer using only the retrieved context.

---

# API Endpoints

## Upload Document

```http
POST /api/v1/documents
```

Uploads and indexes a document.

---

## Chat

```http
POST /api/v1/chat
```

Example request:

```json
{
    "document_id": "123456",
    "query": "How does FastAPI handle file uploads?"
}
```

---

# Environment Variables

Create a `.env` file.

```env
API_KEY=your_gemini_api_key

EMBEDDING_MODEL=gemini-embedding-001

CHAT_MODEL=gemini-2.5-flash

QDRANT_URL=http://localhost:6333

QDRANT_COLLECTION=doc_embeddings

QDRANT_API_KEY=

ENVIRONMENT=dev
```

---

# Running the Project

Clone the repository.

```bash
git clone https://github.com/yourusername/repomind.git
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
uvicorn src.main:app --reload
```

---

# Future Improvements

* GitHub repository ingestion
* Semantic code search
* Architecture-aware retrieval
* File citations
* Repository-level chat
* Multi-document chat
* Knowledge bases
* Authentication
* Redis caching
* Docker
* Kubernetes deployment
* CI/CD pipeline
* Monitoring and logging

---

# Learning Goals

This project is designed to explore production-ready AI engineering concepts, including:

* Retrieval-Augmented Generation (RAG)
* Embedding models
* Vector databases
* Semantic search
* Prompt engineering
* FastAPI architecture
* Modular backend design
* LLM integration
* Production AI systems

---

# License

MIT License.
