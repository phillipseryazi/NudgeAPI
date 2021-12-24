from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm.session import Session
from . import schemas, controllers
from storage.database import get_db
from fastapi_jwt_auth import AuthJWT
from typing import List

business_router = APIRouter(prefix="/business", tags=["business"])


@business_router.post("/create", response_model=schemas.Business, status_code=status.HTTP_201_CREATED)
async def create_business(business: schemas.BusinessCreate, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()

    db_business = controllers.get_business(
        name=business.name, email=business.email, db=db)

    if db_business:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="This business name or email is already in use.")

    business.user_id = current_user
    new_business = controllers.create_business(business=business, db=db)
    return new_business


@business_router.get("/owner/{value}", response_model=List[schemas.Business], status_code=status.HTTP_200_OK)
async def get_businesses_by_owner(value: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    business = controllers.get_businesses_by_owner(id=value, db=db)

    if not business:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Business does not exist.")

    return business


@business_router.get("/id/{value}", response_model=schemas.Business, status_code=status.HTTP_200_OK)
async def get_business_by_id(value: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    business = controllers.get_business_by_id(id=value, db=db)

    if not business:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Business does not exist.")

    return business


@business_router.get("/name", response_model=List[schemas.Business], status_code=status.HTTP_200_OK)
async def get_businesses_by_name(q: str, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    businesses = controllers.get_businesses_by_name(name=q, db=db)

    if not businesses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Business does not exist.")

    return businesses


@business_router.get("/domain", response_model=List[schemas.Business], status_code=status.HTTP_200_OK)
async def get_businesses_by_domain(q: str, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    businesses = controllers.get_businesses_by_domain(domain=q, db=db)

    if not businesses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Business does not exist.")

    return businesses


@business_router.get("/all", response_model=List[schemas.Business], status_code=status.HTTP_200_OK)
async def get_all_businesses(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    businesses = controllers.get_all_businesses(db=db)

    if not businesses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No businesses found.")

    return businesses


@business_router.put("/update", response_model=schemas.Business, status_code=status.HTTP_200_OK)
async def update_business(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    pass
