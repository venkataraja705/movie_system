import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    MONGODB_URL: str
    MONGODB_NAME: str
    MONGODB_COLLECTION: str

    class Config:
        env_file = ".env"

# Load environment variables based on the file specified
environment = os.getenv("ENVIRONMENT", "development")
if environment == "testing":
    load_dotenv(".env.test")
else:
    load_dotenv(".env.dev")

settings = Settings()
