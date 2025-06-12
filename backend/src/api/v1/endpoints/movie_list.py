from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.schema.movie import MovieList
from src.services.movie_list import get_movie_list

router = APIRouter()

@router.get("/", response_model=list[MovieList])
async def get_movies():
    result = await get_movie_list()
    json_compatible_item_data = jsonable_encoder(result)
    return JSONResponse(content=json_compatible_item_data, status_code=200)
