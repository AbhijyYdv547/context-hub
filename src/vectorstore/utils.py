import uuid

from qdrant_client.models import PointStruct, Filter, FieldCondition, MatchValue, PointVectors
from .client import client
from datetime import datetime

from langchain_qdrant import QdrantVectorStore
from src.config import settings
from embeddings.service import get_embedding_model

def index_documents(chunks):
    return QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=get_embedding_model(),
        url=settings.qdrant_url,
        collection_name=settings.qdrant_collection,
    )

def update_voice(id, new_centroid):
    client.update_vectors(
        collection_name="doc_embeddings",
        points=[
            PointVectors(
                id=id,
                vector=new_centroid
            )
        ]
    )


def upsert_voice(centroid, user_id, type="embedding"):
    curr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    client.upsert(
        collection_name="doc_embeddings",
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=centroid,
                payload={
                    "speaker": user_id,
                    "timestamp": curr,
                    "type": type
                }
            )
        ]
    )


def search_voice(embedding):
    res = client.query_points(
        collection_name="doc_embeddings",
        query=embedding,
        limit=5,
        with_payload=True
    )
    return res.points


def get_user_centroid(user_id: str):
    point,_ = client.scroll(
        collection_name="doc_embeddings",
        scroll_filter=Filter(
            must=[
                FieldCondition(
                    key="speaker",
                    match=MatchValue(value=user_id)
                ),
                FieldCondition(
                    key="type",
                    match=MatchValue(value="centroid")
                )
            ]
        ),
        with_vectors=True,
        limit=1
    )

    if not point:
        return None

    return point[0]