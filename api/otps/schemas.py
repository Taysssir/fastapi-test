from pydantic import BaseModel, Field


class CreateOTP(BaseModel):
    recipient_id: str = Field(..., example="taysir.boubaker2082@gmail.com")


class VerifyOTP(CreateOTP):
    session_id: str
    otp_code: str


class InfoOTP(VerifyOTP):
    status: str

