from datetime import datetime, timedelta
from fastapi_jwt_auth import AuthJWT


def generate_auth_tokens(user_id: int, Authorize: AuthJWT):
    access_token = Authorize.create_access_token(
        subject=user_id,
        algorithm="HS256",
        expires_time=timedelta(minutes=30))

    refresh_token = Authorize.create_refresh_token(
        subject=user_id,
        algorithm="HS256",
        expires_time=timedelta(hours=24))

    return {"access_token": access_token, "refresh_token": refresh_token}
