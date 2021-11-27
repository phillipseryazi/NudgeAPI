from fastapi import FastAPI
from app.authentication import views as auth_views

app = FastAPI()

app.include_router(auth_views.router, prefix="/api/v1/auth")
