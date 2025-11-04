import os
from pydantic import BaseModel


class Settings(BaseModel):
    app_env: str = os.getenv("APP_ENV", "local")
    secret_key: str = os.getenv("SECRET_KEY", "dev-secret-change-me")

    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
    refresh_token_expire_days: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "14"))

    cors_origins: list[str] = os.getenv("BACKEND_CORS_ORIGINS", "http://localhost:5173").split(",")

    database_url: str = os.getenv("DATABASE_URL", "postgresql+psycopg://finstop:finstop@db:5432/finstop")
    redis_url: str = os.getenv("REDIS_URL", "redis://redis:6379/0")

    otp_ttl_seconds: int = int(os.getenv("OTP_TTL_SECONDS", "300"))
    otp_max_attempts: int = int(os.getenv("OTP_MAX_ATTEMPTS", "5"))

    s3_endpoint: str | None = os.getenv("S3_ENDPOINT")
    s3_access_key: str | None = os.getenv("S3_ACCESS_KEY")
    s3_secret_key: str | None = os.getenv("S3_SECRET_KEY")
    s3_bucket: str | None = os.getenv("S3_BUCKET")
    s3_region: str | None = os.getenv("S3_REGION")


settings = Settings()

