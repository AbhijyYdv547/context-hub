from pathlib import Path
from langchain_docling.loader import DoclingLoader
from langchain_community.document_loaders import TextLoader

DOCLING_EXTENSIONS = {".pdf", ".docx", ".pptx", ".md", ".html"}

TEXT_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".java",
    ".cpp",
    ".c",
    ".go",
    ".rs",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".txt",
}

def parse_document(file_path: Path):
    extension = file_path.suffix.lower()
    docs = []

    if extension in DOCLING_EXTENSIONS:
        docs = DoclingLoader(file_path=file_path).load()

    elif extension in TEXT_EXTENSIONS:
        docs = TextLoader(file_path=file_path).load()

    else:
        raise ValueError("Unsupported file type")
    
    return docs