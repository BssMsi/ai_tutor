from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.schemas.documents import DocumentResponse

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/", response_model=DocumentResponse, status_code=202)
async def upload_document(plan_id: str, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    """
    Upload a document for processing.
    """
    mock_doc = {
        "id": "mock-doc-uuid",
        "plan_id": plan_id,
        "filename": file.filename,
        "status": "processing",
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": None
    }
    return mock_doc

@router.get("/{document_id}/status", response_model=DocumentResponse)
async def get_document_status(document_id: str, db: AsyncSession = Depends(get_db)):
    """
    Poll document processing status.
    """
    mock_doc = {
        "id": document_id,
        "plan_id": "mock-plan-uuid",
        "filename": "textbook.pdf",
        "status": "ready",
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": "2026-01-01T00:05:00Z"
    }
    return mock_doc
