from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class AnalyzePayload(BaseModel):
    dataset_id: str
    tools: list[str]
    params: dict | None = None


class AnalyzeResult(BaseModel):
    analysis_id: str
    job_id: str


@router.get("/tools", response_model=dict)
def list_tools() -> dict:
    return {
        "tools": [
            "ratios",
            "trends",
            "vertical",
            "horizontal",
            "dupont",
            "cashflow",
            "forecast",
            "valuation",
            "sensitivity",
            "kpi",
            "custom",
        ]
    }


@router.post("/analyze", response_model=AnalyzeResult)
def analyze(payload: AnalyzePayload) -> AnalyzeResult:
    return AnalyzeResult(analysis_id="stub-analysis", job_id="job-analyze-stub")


@router.get("/analyze/status/{job_id}", response_model=dict)
def analyze_status(job_id: str) -> dict:
    return {"status": "queued", "progress": 0}


@router.get("/analyses/{analysis_id}", response_model=dict)
def get_analysis(analysis_id: str) -> dict:
    return {
        "id": analysis_id,
        "summary": "Executive summary stub",
        "metrics": {"roe": 0.15},
        "charts": [],
        "tables": [],
    }

