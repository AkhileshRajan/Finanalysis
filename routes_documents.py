from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class CreateDocumentPayload(BaseModel):
    s3_key: str
    filename: str
    mime: str
    size: int
    sha256: str


class DocumentResponse(BaseModel):
    id: str
    filename: str
    mime: str
    size: int
    status: str
    uploaded_at: str


@router.post("/documents", response_model=DocumentResponse)
def create_document(payload: CreateDocumentPayload) -> DocumentResponse:
    # Stub implementation
    return DocumentResponse(
        id="doc-stub-id",
        filename=payload.filename,
        mime=payload.mime,
        size=payload.size,
        status="uploaded",
        uploaded_at="2024-01-01T00:00:00Z",
    )


@router.get("/documents/{document_id}", response_model=DocumentResponse)
def get_document(document_id: str) -> DocumentResponse:
    # Stub implementation
    return DocumentResponse(
        id=document_id,
        filename="stub.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        size=1024,
        status="uploaded",
        uploaded_at="2024-01-01T00:00:00Z",
    )

