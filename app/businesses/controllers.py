from sqlalchemy.orm.session import Session
from . import schemas, models
from .models import Business
from app import businesses


def create_business(business: schemas.BusinessCreate, db: Session):
    new_business = Business(**business.dict())
    db.add(new_business)
    db.commit()
    db.refresh(new_business)
    return new_business


def get_business_by_owner(id: int, db: Session):
    businesses = db.query(models.Business).filter(
        models.Business.user_id == id).all()

    return businesses


def get_business_by_id(id: int, db: Session):
    business = db.query(models.Business).filter(
        models.Business.id == id).first()

    return business


def get_businesses_by_name(name: str, db: Session):
    pass


def get_businesses_by_domain(domain: str, db: Session):
    pass


def get_all_businesses(db: Session):
    pass


def update_business(business: schemas.BusinessCreate, db: Session):
    pass
