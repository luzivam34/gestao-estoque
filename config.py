import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("Secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATION = False
