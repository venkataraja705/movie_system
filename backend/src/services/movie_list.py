'''
to get movie list from data base
i.e mongodb
'''
from src.schema.movie import MovieList
from src.db.mongodb import Database
from src.config import settings
from fastapi.logger import logger

async def get_movie_list() -> MovieList:
    '''
    To get movie list
    '''
    logger.info("MovieList: initiating dataBase connection")
    movie_list: list = []
    db = Database(db_name=settings.MONGODB_NAME, collection_name=settings.MONGODB_COLLECTION, uri=settings.MONGODB_URL)
    result = await db.find_documents({})
    for val in result:
        movie_list.append(MovieList(id=str(val["_id"]),title=val["title"], poster= val.get("poster", "no image")))
    logger.info("MovieList: Response is done")
    return movie_list[0:20]
