from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class PresignUploadPayload(BaseModel):
    filename: str
    mime: str
    size: int
    sha256: str


class PresignUploadResponse(BaseModel):
    upload_url: str
    s3_key: str


@router.post("/presign-upload", response_model=PresignUploadResponse)
def presign_upload(payload: PresignUploadPayload) -> PresignUploadResponse:
    # Stub presigned URL
    return PresignUploadResponse(upload_url="https://example.com/upload", s3_key="uploads/stub-key")

