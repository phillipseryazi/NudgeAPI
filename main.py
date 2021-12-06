from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.authentication import views as auth_views

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_views.router, prefix="/api/v1/auth")
