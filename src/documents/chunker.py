from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import settings

def chunk_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )
    return splitter.split_documents(documents=docs)