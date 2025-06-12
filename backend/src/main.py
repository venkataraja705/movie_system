'''
Fast API
plan1:
application with capability to demonstrate
a food ordering system
with
- 1 list of food items
- 2 adding food items to cart
- 3 invoice billing with items in cart
- 4 submit to save order with new invoice number to be store

plan2:
1. we connect to mongodb server
2. we fetch  list of documents for movies collection from cloud
3. display in front end react js

'''
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.app import api_router


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more detailed logs
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Logs to console
        logging.FileHandler("app.log")  # Logs to a file
    ]
)

app = FastAPI(title="Your FastAPI App")

# Allow CORS for React app running on localhost:3000
origins = [
    "http://localhost:3000",  # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI Movies Collection application!"}



