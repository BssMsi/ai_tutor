from sqlalchemy import Column, Integer, String, Enum, JSON, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
import enum
from src.models.base import Base

class OnboardingStatus(enum.Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    completed_minimum = "completed_minimum"
    completed_full = "completed_full"

class OnboardingState(Base):
    __tablename__ = "onboarding_states"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    plan_id = Column(String, index=True, nullable=True) # UUID string or similar
    status = Column(Enum(OnboardingStatus), default=OnboardingStatus.not_started)
    collected_params = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    timezone = Column(String, default="UTC")
    max_hours_per_day = Column(Integer, default=4)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class PsychProfile(Base):
    __tablename__ = "psych_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True, nullable=False)
    learning_style_vector = Column(JSON, default=[])
    stress_tolerance = Column(Integer, default=50) # 0-100 scale
    procrastination_index = Column(Integer, default=50) # 0-100 scale
    strengths_weaknesses = Column(JSON, default={"strengths": [], "weaknesses": []})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
