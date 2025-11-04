from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, model_validator


router = APIRouter()


class RequestOtpPayload(BaseModel):
    email: EmailStr | None = None
    phone: str | None = None

    @model_validator(mode="after")
    def validate_email_or_phone(self):
        if not self.email and not self.phone:
            raise ValueError("Either email or phone must be provided")
        return self


class RequestOtpResponse(BaseModel):
    request_id: str
    ttl: int


class VerifyOtpPayload(BaseModel):
    request_id: str
    code: str


class RefreshTokenPayload(BaseModel):
    refresh_token: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


@router.post("/request-otp", response_model=RequestOtpResponse)
def request_otp(payload: RequestOtpPayload) -> RequestOtpResponse:
    # Stub implementation
    return RequestOtpResponse(request_id="stub-request-id", ttl=300)


@router.post("/verify-otp", response_model=TokenResponse)
def verify_otp(payload: VerifyOtpPayload) -> TokenResponse:
    # Stub implementation
    return TokenResponse(access_token="stub-access", refresh_token="stub-refresh")


@router.post("/refresh", response_model=TokenResponse)
def refresh_token(payload: RefreshTokenPayload) -> TokenResponse:
    # Stub implementation
    return TokenResponse(access_token="stub-access", refresh_token="stub-refresh")

