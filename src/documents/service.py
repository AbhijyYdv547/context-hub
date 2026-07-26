from pathlib import Path
from src.documents.parser import parse_pdf
from src.documents.chunker import chunk_documents
from src.vectorstore.utils import index_documents

def ingest_pdf(file_path: Path):
    docs = parse_pdf(file_path)
    chunks = chunk_documents(docs)
    index_documents(chunks)
    return {"status": "indexed", "chunks": len(chunks)}