from fastapi import APIRouter, Request, Query
from fastapi.responses import JSONResponse
from services.openai_service import getGPTAnswer

router = APIRouter()

@router.get('/getAnswer', summary="Get Answer from OpenAI", description="Get a short answer based on the input text using OpenAI.")
async def get_answer_route(request: Request, text: str = Query(..., description="The input text for which the answer is needed.")):
    prompt = "Выведи кратко только ответ. ОТВЕТ МОЖЕТ БЫТЬ ТОЛЬКО ОДИН."
    answer = getGPTAnswer(prompt, text)
    return JSONResponse(content={"answer": answer})
