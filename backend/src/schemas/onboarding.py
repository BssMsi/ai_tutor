from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from src.models.onboarding import OnboardingStatus
from src.schemas.base import ORMModel
from datetime import datetime

class OnboardingStateBase(ORMModel):
    user_id: str
    plan_id: Optional[str] = None
    status: OnboardingStatus = OnboardingStatus.not_started
    collected_params: Dict[str, Any] = {}

class OnboardingStateResponse(OnboardingStateBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

class OnboardingUpdateRequest(BaseModel):
    collected_params: Dict[str, Any]

class StudentProfileBase(ORMModel):
    user_id: str
    name: Optional[str] = None
    timezone: str = "UTC"
    max_hours_per_day: int = 4

class StudentProfileResponse(StudentProfileBase):
    id: int
    created_at: datetime

class PsychProfileBase(ORMModel):
    user_id: str
    learning_style_vector: List[float] = []
    stress_tolerance: int = Field(default=50, ge=0, le=100)
    procrastination_index: int = Field(default=50, ge=0, le=100)
    strengths_weaknesses: Dict[str, List[str]] = {"strengths": [], "weaknesses": []}

class PsychProfileResponse(PsychProfileBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
