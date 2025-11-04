from celery import Celery
from app.core.config import settings


celery_app = Celery(
    "finstop",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
)


@celery_app.task
def parse_document_task(document_id: str) -> dict:
    return {"dataset_id": "stub-dataset", "document_id": document_id}


@celery_app.task
def analyze_task(dataset_id: str, tools: list[str]) -> dict:
    return {"analysis_id": "stub-analysis", "dataset_id": dataset_id, "tools": tools}


@celery_app.task
def export_task(analysis_id: str, fmt: str) -> dict:
    return {"export_id": "stub-export", "format": fmt}

