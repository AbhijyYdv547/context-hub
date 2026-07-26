from src.chat.prompt import build_system_prompt
from src.chat.schemas import ChatRequest
from src.llm.base import client
from src.config import settings
from src.vectorstore.service import search_documents


async def chat(request: ChatRequest):
        document_id = request.document_id
        query = request.query
    
        result = search_documents(query, document_id)

        if not result:
            return "I couldn't find any relevant information in this document."
    
        context =  "\n\n".join(
            res["text"]
            for res in result
        )

        prompt = build_system_prompt(context)

        response = await client.chat.completions.create(
        model=settings.chat_model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ]
        )
    
        return response.choices[0].message.content