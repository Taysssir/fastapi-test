import uuid
from fastapi import APIRouter, HTTPException
from api.otps import schemas
from api.utils import otpUtil, emailUtil
from api.otps import crud
from api.auth import crud as crudAuth

router = APIRouter(
    prefix='/api/v1'
)


@router.post("/otp/send", include_in_schema=False)
async def send_otp(
    request: schemas.CreateOTP
):
    # Generate 4 digits and save to table OTPs
    otp_code = otpUtil.random(4)
    session_id = str(uuid.uuid1())
    await crud.save_otp(request, session_id, otp_code)
    # Send OTP VIA email
    subject = "OTP Code"
    recipient = request.recipient_id
    # recipient = [request.recipient_id]
    message = """
        <!DOCTYPE html>
        <html>
        <title>Verify Account</title>
        <body>
        <div style="width:100%;font-family: monospace;">
            <h1>{0:}</h1>
        </div>
        </body>
        </html>
        """.format(otp_code)
    print("Sending OTP Code via Email : {0} ".format(otp_code))
    print(message)
    # await emailUtil.send_email(subject, [recipient], message)
    return {
        "recipient_id":recipient,
        "session_id": session_id,
        "otp_code": otp_code
    }


@router.post("/otp/verify")
async def verify_otp(request: schemas.VerifyOTP):

    # Check OTP code 4 digit life time equalTo 1 minute
    otp_result = await crud.find_otp_life_time(request.recipient_id, request.session_id)
    if not otp_result:
        raise HTTPException(status_code=404, detail="OTP code has expired, please request a new one.")

    otp_result = schemas.InfoOTP(**otp_result)
    
    # Update User Acount Status TO '1' : Account Activated
    update_result = await crudAuth.update_user(request.recipient_id)
    
    # Check if OTP code is already used
    if otp_result.status == "9":
        raise HTTPException(status_code=404, detail="OTP code has used, please request a new one.")

    # Disable otp code when succeed verified
    await crud.disable_otp(otp_result)

    return {
        "status_code": 200,
        "detail": "OTP verified successfully"
    }
