from fastapi import APIRouter, status, Depends
from sqlalchemy.orm.session import Session
from . import schemas, controllers
from storage.database import get_db
from fastapi_jwt_auth import AuthJWT

business_router = APIRouter(prefix="/business", tags=["business"])


@business_router.post("/create", response_model=schemas.Business, status_code=status.HTTP_201_CREATED)
async def create_business(business: schemas.BusinessCreate, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    business.user_id = current_user
    new_business = controllers.create_business(business=business, db=db)
    return new_business


@business_router.get("/owner/{value}", response_model=schemas.Business, status_code=status.HTTP_200_OK)
async def get_business_by_owner(value: int, db: Session = Depends(get_db)):
    business = controllers.get_business_by_owner(id=value, db=db)
    return business


@business_router.get("/id/{value}", response_model=schemas.Business, status_code=status.HTTP_200_OK)
async def get_business_by_id(value: int, db: Session = Depends(get_db)):
    business = controllers.get_business_by_id(id=value, db=db)
    return business


@business_router.get("/name/{value}", response_model=schemas.Business, status_code=status.HTTP_200_OK)
async def get_businesses_by_name(value: str, db: Session = Depends(get_db)):
    businesses = controllers.get_businesses_by_name(name=value, db=db)
    return businesses


@business_router.get("/domain/{value}", response_model=schemas.Business, status_code=status.HTTP_200_OK)
async def get_businesses_by_domain(value: str, db: Session = Depends(get_db)):
    businesses = controllers.get_businesses_by_domain(domain=value, db=db)
    return businesses


@business_router.get("/all", response_model=schemas.Business, status_code=status.HTTP_200_OK)
async def get_all_businesses(db: Session = Depends(get_db)):
    businesses = controllers.get_all_businesses(db=db)
    return businesses


@business_router.put("/update", response_model=schemas.Business, status_code=status.HTTP_200_OK)
async def update_business():
    pass
