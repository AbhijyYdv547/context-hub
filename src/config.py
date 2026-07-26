from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    qdrant_url: str
    qdrant_api_key: str

    qdrant_collection: str = "doc_collections"

    gemini_api_key: str

    chat_model: str = "gemini-2.5-flash"

    chunk_size: int = 800

    chunk_overlap: int = 150

    environment: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()