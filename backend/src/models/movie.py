'''
Item which will have 
a structure similar to 
{"_id":{"$oid":"573a1391f29313caabcd6e2a"},
"plot":"A newly wedded couple attempt to build a house with a prefabricated kit, unaware that a rival sabotaged the kit's component numbering.",
"genres":["Short","Comedy"],
"runtime":{"$numberInt":"25"},
"cast":["Buster Keaton","Sybil Seely"],
"num_mflix_comments":{"$numberInt":"0"},
"title":"One Week","fullplot":"Buster and Sybil exit a chapel as newlyweds. Among the gifts is a portable house you easily put together in one week. It doesn't help that Buster's rival for Sybil switches the numbers on the crates containing the house parts.",
"languages":["English"],"released":{"$date":{"$numberLong":"-1556841600000"}},
"directors":["Edward F. Cline","Buster Keaton"],
"rated":"TV-G",
"awards":{"wins":{"$numberInt":"1"},
"nominations":{"$numberInt":"0"},
"text":"1 win."},
"lastupdated":"2015-05-07 01:07:01.633000000",
"year":{"$numberInt":"1920"},
"imdb":{"rating":{"$numberDouble":"8.3"},
"votes":{"$numberInt":"3942"},
"id":{"$numberInt":"11541"}},
"countries":["USA"],
"type":"movie",
"tomatoes":{"viewer":{"rating":{"$numberDouble":"4.3"},
"numReviews":{"$numberInt":"752"},
"meter":{"$numberInt":"91"}},
"lastUpdated":{"$date":{"$numberLong":"1442168539000"}}}}
'''

from pydantic import BaseModel
from typing import List, Optional, Dict

class Movie(BaseModel):
    id: Optional[str] = None  # This will hold the MongoDB ObjectId as a string
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

    class Config:
        orm_mode = True  # This allows Pydantic to work with ORMs

