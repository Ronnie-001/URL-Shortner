# dbconn.py

# import the ORM 
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine

# get environment variables
from dotenv import load_dotenv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.normpath(os.path.join(current_dir, "..", ".."))
dotenv_path = os.path.join(project_root, ".env")

load_dotenv(dotenv_path=dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError(
        "DATABASE_URL is not set."
        "Please check that the .env file exists at the correct path "
        "and contains the DATABASE_URL variable."
    )

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
