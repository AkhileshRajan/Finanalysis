from fastapi import APIRouter

from . import routes_auth, routes_files, routes_documents, routes_parse, routes_analyze, routes_report, routes_me


api_router = APIRouter()

api_router.include_router(routes_auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(routes_files.router, prefix="/files", tags=["files"])
api_router.include_router(routes_documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(routes_parse.router, prefix="", tags=["parse"])
api_router.include_router(routes_analyze.router, prefix="", tags=["analyze"])
api_router.include_router(routes_report.router, prefix="", tags=["report"])
api_router.include_router(routes_me.router, prefix="", tags=["me"])

