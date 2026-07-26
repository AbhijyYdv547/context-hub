from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    qdrant_url: str
    qdrant_api_key: str

    gemini_api_key: str

    environment: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()