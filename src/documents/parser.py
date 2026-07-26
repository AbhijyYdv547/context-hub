from pathlib import Path
from langchain_docling.loader import DoclingLoader

def parse_pdf(file_path: Path):
    loader = DoclingLoader(file_path=file_path)
    return loader.load()