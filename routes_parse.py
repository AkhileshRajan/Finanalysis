from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class ParsePayload(BaseModel):
    document_id: str


class JobResponse(BaseModel):
    dataset_id: str | None = None
    analysis_id: str | None = None
    job_id: str


class JobStatusResponse(BaseModel):
    status: str
    errors: list[str] | None = None
    progress: int | None = None


@router.post("/parse", response_model=JobResponse)
def parse_document(payload: ParsePayload) -> JobResponse:
    return JobResponse(dataset_id="stub-dataset", job_id="job-parse-stub")


@router.get("/parse/status/{job_id}", response_model=JobStatusResponse)
def parse_status(job_id: str) -> JobStatusResponse:
    return JobStatusResponse(status="queued", progress=0)

