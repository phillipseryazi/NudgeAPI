from sqlalchemy.orm import Session
from . import models
from .dependencies import hash_password, verify_password
from . import schemas


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def find_token_in_blacklist(db: Session, token: str):
    return db.query(models.Blacklist).filter(models.Blacklist.token == token).first()


def create_user(user: schemas.UserCreate, db: Session):
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login_user(password, hashed_password):
    is_valid = verify_password(password, hashed_password)

    if not is_valid:
        return None

    return is_valid


def blacklist_token(token: schemas.Blacklist, db: Session):
    blacklist_token = models.Blacklist(token=token)
    db.add(blacklist_token)
    db.commit()


def delete_token(token: schemas.Blacklist, db: Session):
    db.delete(token)
    db.commit()

