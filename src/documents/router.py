from fastapi import UploadFile, File
from typing import Annotated
from src.documents.service import ingest_document
from src.documents.utils import delete_upload_file, save_upload_file
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/documents", tags=["Documents"])

@router.post("/")
async def receive_any_document(file: Annotated[UploadFile, File()]):

    temp_path = save_upload_file(file)

    res = ingest_document(temp_path)

    delete_upload_file(temp_path)

    return res