
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from src.config import settings

if(settings.environment == "dev"):
    client = QdrantClient(path="./qdrant_data")

elif(settings.environment == "production"):
    client = QdrantClient(
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
    )

else:
    raise ValueError(f"Unknown environment: {settings.environment!r}. Expected 'dev' or 'production'.")

collections = client.get_collections().collections
if "voice_embeddings" not in [c.name for c in collections]:
    client.create_collection(
        collection_name="voice_embeddings",
        vectors_config=VectorParams(size=192, distance=Distance.COSINE),
    )

