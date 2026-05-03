from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
import enum
from src.models.base import Base

class PlanStatus(enum.Enum):
    active = "active"
    archived = "archived"

class PlanTaskStatus(enum.Enum):
    pending = "pending"
    done = "done"
    skip = "skip"

class Plan(Base):
    __tablename__ = "plans"

    id = Column(String, primary_key=True, index=True) # String for UUID
    user_id = Column(String, index=True, nullable=False)
    name = Column(String, nullable=False)
    status = Column(Enum(PlanStatus), default=PlanStatus.active)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    tasks = relationship("PlanTask", back_populates="plan", cascade="all, delete-orphan")

class PlanTask(Base):
    __tablename__ = "plan_tasks"

    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(String, ForeignKey("plans.id"), nullable=False)
    topic = Column(String, nullable=False)
    scheduled_date = Column(DateTime(timezone=True), nullable=False)
    estimated_minutes = Column(Integer, default=30)
    status = Column(Enum(PlanTaskStatus), default=PlanTaskStatus.pending)
    revision_round = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    plan = relationship("Plan", back_populates="tasks")
