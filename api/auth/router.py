import uuid
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from api.auth import schemas
from api.auth import crud
from api.otps import router as otpsRouter
from api.otps import schemas as otpsSchemas
from api.utils import cryptoUtil, constantUtil, jwtUtil
from api.exceptions.business import BusinessException

router = APIRouter(
    prefix='/api/v1'
)

@router.post("/auth/register")
async def register(user: schemas.UserCreate):
    row = await crud.find_existed_user(user.email)
    if row:
        raise BusinessException(status_code=999, detail="User already registered!")

    # Create new user
    user.password = cryptoUtil.get_password_hash(user.password)
    await crud.save_user(user)
    # Send OTP code for user Via email
    otpsSchemas.CreateOTP.recipient_id = user.email
    otpSend = await otpsRouter.send_otp(otpsSchemas.CreateOTP)
    return otpSend
    
@router.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await crud.find_existed_user(form_data.username)
    if not user:
        raise BusinessException(status_code=999, detail="User not found")
    if user.status == '0' : 
        raise BusinessException(status_code=999, detail="User Account not activated")
    user = schemas.UserPWD(**user)
    is_valid = cryptoUtil.verify_password(form_data.password, user.password)
    if not is_valid:
        raise BusinessException(status_code=999, detail="Incorrect username or password")

    access_token_expires = jwtUtil.timedelta(minutes=constantUtil.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await jwtUtil.create_access_token(
        data={"sub": form_data.username},
        expires_delta=access_token_expires,
    )

    results = {
        "access_token": access_token,
        "token_type": "bearer"
    }

    results.update({
        "user_info": {
            "email": user.email,
            "fullname": user.fullname
        }
    })

    return results
