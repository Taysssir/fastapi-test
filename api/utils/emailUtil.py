from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from starlette.config import Config
# from starlette.config import TwilioConfig
# from twilio.rest import Client
from typing import List


config = Config('api/.env')
conf = ConnectionConfig(
    MAIL_USERNAME=config("MAIL_USERNAME"),
    MAIL_PASSWORD=config("MAIL_PASSWORD"),
    MAIL_FROM=config("MAIL_FROM"),
    MAIL_PORT=config("MAIL_PORT"),
    MAIL_SERVER=config("MAIL_SERVER"),
    USE_CREDENTIALS=config("USE_CREDENTIALS")
)

# MAIL_SSL_TLS=config("MAIL_SSL_TLS"),
# MAIL_STARTTLS=config("MAIL_STARTTLS"),
# MAIL_STARTTLS = True,
# MAIL_SSL_TLS = False,
# USE_CREDENTIALS = True

# settings = TwilioConfig.Settings()
# client = Client(settings.twilio_account_sid, settings.twilio_auth_token)


async def send_email(subject: str, recipient: List, message: str):
    message = MessageSchema(
        subject=subject,
        recipients=recipient,
        body=message,
        subtype="html"
    )
    print(message)
    fm = FastMail(conf)
    await fm.send_message(message)
