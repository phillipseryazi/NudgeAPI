from fastapi import APIRouter, status, Depends
from . import schemas

business_router = APIRouter(prefix="/business", tags=["business"])


@business_router.post("/create", response_model=schemas.Business, status_code=status.HTTP_201_CREATED)
def create_business():
    pass


@business_router.put("/update", response_model=schemas.Business, status_code=status.HTTP_200_OK)
def update_business():
    pass
