from typing import Optional, List
from pydantic import BaseModel
from src.models.plans import PlanStatus, PlanTaskStatus
from src.schemas.base import ORMModel
from datetime import datetime

class PlanTaskBase(ORMModel):
    topic: str
    scheduled_date: datetime
    estimated_minutes: int = 30
    status: PlanTaskStatus = PlanTaskStatus.pending
    revision_round: int = 1

class PlanTaskCreate(PlanTaskBase):
    pass

class PlanTaskResponse(PlanTaskBase):
    id: int
    plan_id: str
    created_at: datetime

class PlanBase(ORMModel):
    user_id: str
    name: str
    status: PlanStatus = PlanStatus.active

class PlanCreate(PlanBase):
    pass

class PlanResponse(PlanBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime]
    tasks: List[PlanTaskResponse] = []
