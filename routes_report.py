from fastapi import APIRouter
from pydantic import BaseModel, field_validator


router = APIRouter()


class ExportPayload(BaseModel):
    analysis_id: str
    format: str

    @field_validator("format")
    @classmethod
    def validate_format(cls, v: str) -> str:
        if v not in ["xlsx", "pdf"]:
            raise ValueError("format must be 'xlsx' or 'pdf'")
        return v


@router.post("/report/export", response_model=dict)
def export_report(payload: ExportPayload) -> dict:
    return {"job_id": "job-export-stub"}


@router.get("/report/export/status/{job_id}", response_model=dict)
def export_status(job_id: str) -> dict:
    return {"status": "queued"}


@router.get("/report/download/{export_id}", response_model=dict)
def report_download(export_id: str) -> dict:
    return {"download_url": "https://example.com/download/stub"}

