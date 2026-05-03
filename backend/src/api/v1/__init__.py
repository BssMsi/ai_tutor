from fastapi import APIRouter

from src.api.v1.chat import router as chat_router
from src.api.v1.onboarding import router as onboarding_router
from src.api.v1.plans import router as plans_router
from src.api.v1.documents import router as documents_router
from src.api.v1.webhooks import router as webhooks_router

api_router = APIRouter()
api_router.include_router(chat_router)
api_router.include_router(onboarding_router)
api_router.include_router(plans_router)
api_router.include_router(documents_router)
api_router.include_router(webhooks_router)
