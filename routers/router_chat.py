from fastapi import APIRouter
from fastapi import status as response_status
from fastapi import Body
from utils.GeminiChatbot import GeminiChatbot


router = APIRouter(prefix="/chatbot", tags=["tag"])


@router.get("/response", status_code=response_status.HTTP_200_OK)
async def get_response(user_input: str = Body(..., embed=True)):
    chatbot = GeminiChatbot()
    response = chatbot.generate_response(user_input)
    return {"response": response}
