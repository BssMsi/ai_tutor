from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import asyncio

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    user_id: str
    plan_id: str
    messages: list[ChatMessage]

async def mock_stream_response():
    chunks = [
        {"type": "ui_hint", "data": "highlight_planner"},
        {"type": "text", "data": "Let's review "},
        {"type": "text", "data": "your study schedule."},
    ]
    for chunk in chunks:
        yield f"data: {chunk}\n\n"
        await asyncio.sleep(0.5)

@router.post("/stream")
async def chat_stream(request: ChatRequest):
    """
    Main entry point for chat. Streams responses.
    """
    return StreamingResponse(mock_stream_response(), media_type="text/event-stream")
