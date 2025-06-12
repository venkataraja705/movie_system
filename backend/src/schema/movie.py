'''
schema where we use for type validation
'''

from pydantic import BaseModel
from typing import List, Optional, Dict

class Movie(BaseModel):
    id: Optional[str] 
    title: str
    plot: str
    genres: List[str]
    runtime: int  # Assuming runtime is stored as an integer (in minutes)
    cast: List[str]
    directors: List[str]
    released: Optional[str]  # Could be a date string or more structured
    year: int
    imdb_rating: float
    imdb_votes: int
    awards: Dict[str, int]  # Dictionary for awards info
    languages: List[str]
    countries: List[str]
    type: str
    tomatoes: Dict[str, dict]  # Dictionary for tomato ratings and reviews

class MovieList(BaseModel):
    id: Optional[str]
    title: str
    poster: str

class MovieDetails(Movie):
    pass
    