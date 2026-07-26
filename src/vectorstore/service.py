import uuid

from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.models import FieldCondition, Filter, MatchValue, PointStruct
from src.vectorstore.client import client
from datetime import datetime

from src.config import settings
from src.embeddings.service import get_embedding_model

def create_collection():
    collections = client.get_collections().collections
    if settings.qdrant_collection not in [c.name for c in collections]:
        client.create_collection(
            collection_name=settings.qdrant_collection,
            vectors_config=VectorParams(size=192, distance=Distance.COSINE),
        )


def index_documents(chunks, document_id):
    curr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    embedding_model = get_embedding_model()

    texts = [chunk.page_content for chunk in chunks]
    vectors = embedding_model.embed_documents(texts)
    points= []

    for chunk, vector in zip(chunks, vectors):
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "document_id": document_id,
                    "text": chunk.page_content,
                    "timestamp": curr,
                    "page": chunk.metadata.get("page")
                } 
            )
        )

    return client.upsert(
        collection_name=settings.qdrant_collection,
        points=points
    )


def search_documents(query, document_id):
    embedding_model = get_embedding_model()
    query_vector = embedding_model.embed_query(query)
    res = client.query_points(
        collection_name=settings.qdrant_collection,
        query=query_vector,
        limit=5,
        query_filter=Filter(
            must=[
                FieldCondition(
                    key="document_id",
                    match=MatchValue(value=document_id)
                )
            ]
        )
    )
    return [
        {
            "score": point.score,
            **point.payload
        }
        for point in res.points
    ]