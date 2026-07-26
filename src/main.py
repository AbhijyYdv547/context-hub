from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.documents.router import router as document_router
from src.chat.router import router as chat_router
from src.vectorstore.service import create_collection

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_collection()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(document_router)
app.include_router(chat_router)


