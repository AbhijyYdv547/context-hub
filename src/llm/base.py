from openai import OpenAI
from src.config import settings

client = OpenAI(
    api_key= settings.api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

