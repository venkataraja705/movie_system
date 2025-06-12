from fastapi import APIRouter
from src.api.v1.endpoints import movie_list

api_router = APIRouter()

api_router.include_router(movie_list.router, prefix="/movielist", tags=["APP"])
