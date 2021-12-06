from datetime import timedelta
from fastapi_jwt_auth import AuthJWT


def generate_access_token(user_id: int, Authorize: AuthJWT):
    return Authorize.create_access_token(subject=user_id, algorithm="HS256", expires_time=timedelta(hours=24))


def generate_refresh_token(user_id: int, Authorize: AuthJWT):
    return Authorize.create_refresh_token(subject=user_id, algorithm="HS256", expires_time=timedelta(days=7))
