import shutil

from fastapi import UploadFile, File
from typing import Annotated
from pathlib import Path
import tempfile

def save_upload_file(file: Annotated[UploadFile, File()]):
    temp_dir = Path(tempfile.gettempdir())
    temp_path = temp_dir / file.filename
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return temp_path

def delete_upload_file(file_path: Path):
    if file_path.is_file():
        file_path.unlink()
        print("File deleted successfully.")
    else:
        print("File not found.")