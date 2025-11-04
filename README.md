# Finstop by Akhilesh Rajan

One-stop financial analysis. This repo currently includes a backend API skeleton (FastAPI + Celery) and Docker Compose for local development.

## Stack

- Backend: FastAPI (Python 3.11), Celery, Redis, PostgreSQL
- Parsing: pandas, openpyxl, pdfplumber, camelot/tabula (stubs for now)
- Infra: Docker Compose

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Git (for cloning)

### Setup

1) Clone the repository:
```bash
git clone <your-repo-url>
cd finstop
```

2) Create an environment file `.env` in the project root (same directory as `docker-compose.yml`). Copy from `.env.example` if available, or use these values:

```bash
APP_ENV=local
SECRET_KEY=change-this-to-a-strong-random-secret-key-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=14
BACKEND_CORS_ORIGINS=http://localhost:5173,http://localhost:3000
DATABASE_URL=postgresql+psycopg://finstop:finstop@db:5432/finstop
REDIS_URL=redis://redis:6379/0
OTP_TTL_SECONDS=300
OTP_MAX_ATTEMPTS=5
```

**⚠️ Security Note:** Never commit `.env` files to version control. The `.gitignore` file is configured to exclude them.

3) Build and run services:

```bash
docker compose up --build
```

4) API will be available at `http://localhost:8000` with interactive docs at `http://localhost:8000/docs`.

## API Endpoints (stubs)

- **Auth**: `/api/v1/auth/request-otp`, `/api/v1/auth/verify-otp`, `/api/v1/auth/refresh`
- **Files**: `/api/v1/files/presign-upload`
- **Documents**: `/api/v1/documents` (POST), `/api/v1/documents/{id}` (GET)
- **Parse**: `/api/v1/parse`, `/api/v1/parse/status/{job_id}`
- **Analyze**: `/api/v1/tools`, `/api/v1/analyze`, `/api/v1/analyze/status/{job_id}`, `/api/v1/analyses/{analysis_id}`
- **Report**: `/api/v1/report/export`, `/api/v1/report/export/status/{job_id}`, `/api/v1/report/download/{export_id}`
- **Misc**: `/api/v1/me`, `/health`

All endpoints currently return stub data to validate the flow. Replace stubs with real logic incrementally.

## Development Notes

- Backend code lives in `backend/app/`.
- Celery worker runs with the same image; see `docker-compose.yml`.
- Add actual S3 provider and presigning later; currently returns placeholders.
- Python cache files (`__pycache__/`) are excluded from version control.

## Security

- All secrets should be provided via environment variables
- Default `SECRET_KEY` in config is for development only - **must be changed in production**
- Database credentials in docker-compose are for local development only
- `.env` files are excluded from git (see `.gitignore`)

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/v1/          # API routes
│   │   ├── core/             # Configuration
│   │   ├── celery_app.py     # Celery tasks
│   │   └── main.py           # FastAPI app
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── .gitignore
├── LICENSE
└── README.md
```

## Next Steps

- Implement OTP storage/verification and JWT issuance
- Add S3/MinIO integration for file uploads and report downloads
- Add parsers for Excel/CSV/PDF and normalization pipeline
- Add analysis modules and reporting/export
- Create a React + Vite frontend
- Add database migrations (Alembic)
- Add tests

## License

MIT License - see LICENSE file for details.

