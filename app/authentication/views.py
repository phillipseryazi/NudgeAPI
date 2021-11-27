from datetime import datetime, timedelta
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from . import schemas
from storage.database import get_db
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from . import controllers
from utils.security import generate_auth_tokens

router = APIRouter(tags=["users", "authentication"])


@AuthJWT.load_config
def get_config():
    return schemas.Settings()


@router.post("/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    db_user = controllers.get_user_by_email(db=db, email=user.email)

    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="This email already exists")

    new_user = controllers.create_user(db=db, user=user)

    tokens = generate_auth_tokens(new_user.id, Authorize=Authorize)

    return {
        "id": new_user.id,
        "access_token": tokens["access_token"],
        "refresh_token": tokens["refresh_token"]
    }


@router.post("/login", response_model=schemas.AuthToken, status_code=status.HTTP_200_OK)
def login_user(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    db_user = controllers.get_user_by_email(db=db, email=credentials.username)

    if not db_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid credentials")

    is_valid = controllers.login_user(credentials.password, db_user.password)

    if not is_valid:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid credentials")

    tokens = generate_auth_tokens(db_user.id, Authorize=Authorize)

    return {
        "id": db_user.id,
        "access_token": tokens["access_token"],
        "refresh_token": tokens["refresh_token"]
    }


@router.get("/refresh")
def refresh_token():
    pass
