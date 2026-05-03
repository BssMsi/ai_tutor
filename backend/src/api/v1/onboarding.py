from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict, Any

from src.core.database import get_db
from src.schemas.onboarding import OnboardingStateResponse, OnboardingUpdateRequest, OnboardingStateBase
from src.models.onboarding import OnboardingStatus

router = APIRouter(prefix="/onboarding", tags=["Onboarding"])

@router.get("/{user_id}", response_model=OnboardingStateResponse)
async def get_onboarding_state(user_id: str, db: AsyncSession = Depends(get_db)):
    """
    Get current onboarding state for a user. Returns mocked data for now.
    """
    # Placeholder for DB query
    mock_state = {
        "id": 1,
        "user_id": user_id,
        "plan_id": None,
        "status": OnboardingStatus.not_started,
        "collected_params": {},
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": None
    }
    return mock_state

@router.post("/{user_id}", response_model=OnboardingStateResponse)
async def update_onboarding_state(
    user_id: str, 
    update_data: OnboardingUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Update onboarding state for a user.
    """
    # Placeholder logic
    mock_state = {
        "id": 1,
        "user_id": user_id,
        "plan_id": None,
        "status": OnboardingStatus.in_progress,
        "collected_params": update_data.collected_params,
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": "2026-01-01T00:00:00Z"
    }
    return mock_state
