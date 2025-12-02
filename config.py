import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:root@localhost:5432/users'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SECRET_KEY='your_secret_key'
