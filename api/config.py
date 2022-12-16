from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: str
    DB_CONTAINER: str
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file = "api/.env"
        env_file_encoding = 'utf-8'

# class TwilioSettings(BaseSettings):
#     twilio_account_sid: str
#     twilio_auth_token: str
#     twilio_verify_service: str

#     class TwilioConfig:
#         env_file = '.env'

