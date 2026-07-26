from src.chat.schemas import ChatRequest
from src.chat.service import chat
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/chat", tags=["Chat"])

@router.post("/")
async def receive_query(request: ChatRequest):
    return await chat(request)