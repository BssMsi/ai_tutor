from sqlalchemy import Column, Integer, String, Enum, DateTime, func
import enum
from src.models.base import Base

class DocumentStatus(enum.Enum):
    uploaded = "uploaded"
    processing = "processing"
    ready = "ready"
    failed = "failed"

class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, index=True) # String for UUID
    plan_id = Column(String, index=True, nullable=False)
    filename = Column(String, nullable=False)
    status = Column(Enum(DocumentStatus), default=DocumentStatus.uploaded)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
