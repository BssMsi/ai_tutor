from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.core.database import get_db
from src.schemas.plans import PlanResponse, PlanCreate, PlanTaskResponse, PlanTaskCreate

router = APIRouter(prefix="/plans", tags=["Plans"])

@router.post("/", response_model=PlanResponse)
async def create_plan(plan: PlanCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new study plan.
    """
    mock_plan = {
        "id": "mock-plan-uuid",
        "user_id": plan.user_id,
        "name": plan.name,
        "status": plan.status,
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": None,
        "tasks": []
    }
    return mock_plan

@router.get("/{plan_id}", response_model=PlanResponse)
async def get_plan(plan_id: str, db: AsyncSession = Depends(get_db)):
    """
    Get plan details.
    """
    mock_plan = {
        "id": plan_id,
        "user_id": "mock-user",
        "name": "Mock Plan",
        "status": "active",
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": None,
        "tasks": []
    }
    return mock_plan

@router.post("/{plan_id}/tasks", response_model=PlanTaskResponse)
async def create_task(plan_id: str, task: PlanTaskCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new task within a plan.
    """
    mock_task = {
        "id": 1,
        "plan_id": plan_id,
        "topic": task.topic,
        "scheduled_date": task.scheduled_date,
        "estimated_minutes": task.estimated_minutes,
        "status": task.status,
        "revision_round": task.revision_round,
        "created_at": "2026-01-01T00:00:00Z"
    }
    return mock_task
