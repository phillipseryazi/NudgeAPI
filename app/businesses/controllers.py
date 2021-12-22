from sqlalchemy.orm.session import Session
from sqlalchemy import func
from . import schemas, models
from .models import Business


def get_business(name: str, email: str, db: Session):
    name = db.query(models.Business).filter(
        models.Business.name.like(f"%{name}%")).first()

    email = db.query(models.Business).filter(
        models.Business.email.like(f"%{email}%")).first()

    if name or email:
        return True

    return False


def create_business(business: schemas.BusinessCreate, db: Session):
    new_business = Business(**business.dict())
    db.add(new_business)
    db.commit()
    db.refresh(new_business)
    return new_business


def get_businesses_by_owner(id: int, db: Session):
    try:
        businesses = db.query(models.Business).filter(
            models.Business.user_id == id).all()
        return businesses
    except Exception as e:
        print(e)


def get_business_by_id(id: int, db: Session):
    try:
        business = db.query(models.Business).filter(
            models.Business.id == id).first()
        return business
    except Exception as e:
        print(e)


def get_businesses_by_name(name: str, db: Session):
    try:
        businesses = db.query(models.Business).filter(
            models.Business.name.ilike(f"%{name}%")).all()
        return businesses
    except Exception as e:
        print(e)


def get_businesses_by_domain(domain: str, db: Session):
    try:
        businesses = db.query(models.Business).filter(func.array_to_string(
            models.Business.domain, ",").ilike(func.any_([f"%{domain}%"]))).all()
        return businesses
    except Exception as e:
        print(e)


def get_all_businesses(db: Session):
    try:
        businesses = db.query(models.Business).all()
        return businesses
    except Exception as e:
        print(e)


def update_business(business: schemas.BusinessCreate, db: Session):
    pass
