
from qdrant_client import QdrantClient
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



