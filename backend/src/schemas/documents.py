from typing import Optional
from pydantic import BaseModel
from src.models.documents import DocumentStatus
from src.schemas.base import ORMModel
from datetime import datetime

class DocumentBase(ORMModel):
    plan_id: str
    filename: str
    status: DocumentStatus = DocumentStatus.uploaded

class DocumentCreate(DocumentBase):
    pass

class DocumentResponse(DocumentBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime]
