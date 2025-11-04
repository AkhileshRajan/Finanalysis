from fastapi import APIRouter


router = APIRouter()


@router.get("/me", response_model=dict)
def me() -> dict:
    # Stub user profile
    return {"id": "user-stub", "email": "user@example.com"}

