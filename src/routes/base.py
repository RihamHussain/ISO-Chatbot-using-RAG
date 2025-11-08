from fastapi import FastAPI, APIRouter
from helpers.config import get_settings
Base_Router = APIRouter(
    prefix="/api/v1",
    tags=["chatbot"]
)

@Base_Router.get("/")
async def welcome():
    app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "app_name": app_name, 
        "app_version": app_version
    }