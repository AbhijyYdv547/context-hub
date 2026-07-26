import uuid
from pathlib import Path
from src.documents.parser import parse_document
from src.documents.chunker import chunk_documents
from src.vectorstore.service import index_documents

def ingest_document(path: Path):
    docs = parse_document(path)
    document_id = str(uuid.uuid4())

    chunks = chunk_documents(docs)
    index_documents(chunks, document_id)
    return {
        "docuement_id": document_id,
        "status": "indexed"
    }