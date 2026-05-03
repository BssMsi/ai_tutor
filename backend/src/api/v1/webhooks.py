from fastapi import APIRouter, Request

router = APIRouter(prefix="/webhooks", tags=["Webhooks"])

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    """
    Receive WhatsApp messages.
    """
    payload = await request.json()
    return {"status": "received"}

@router.post("/telegram")
async def telegram_webhook(request: Request):
    """
    Receive Telegram messages.
    """
    payload = await request.json()
    return {"status": "received"}
