from api.utils.dbUtil import database
from api.otps import schemas


def save_otp(
    request: schemas.CreateOTP,
    session_id: str,
    otp_code: str
):
    query = "INSERT INTO my_otps(id, recipient_id, session_id, otp_code, status, created_on) " \
            "VALUES (nextval('otp_id_seq'), :recipient_id, :session_id, :otp_code, '1', now() at time zone 'UTC')"
    return database.execute(query, values={"recipient_id": request.recipient_id, "session_id": session_id, "otp_code": otp_code})


def find_otp_life_time(recipient_id: str, session_id: str):
    query = "select * from my_otps where recipient_id=:recipient_id and session_id=:session_id and " \
            "created_on >= now() at time zone 'utc' - interval '60 minutes'"
    return database.fetch_one(query, values={"recipient_id": recipient_id, "session_id": session_id})


def disable_otp(request: schemas.VerifyOTP):
    query = "UPDATE my_otps SET status='9' where recipient_id=:recipient_id and session_id=:session_id and otp_code=:otp_code"
    return database.execute(query, values={"recipient_id": request.recipient_id, "session_id": request.session_id,
                                          "otp_code": request.otp_code})
