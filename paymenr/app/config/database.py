from sqlalchemy import create_engine  
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.config import Config
from .config import settings

try:
    config = Config(".env")
except FileNotFoundError:
        config = Config()


# for only Postgress database 
SQLALCHEMY_DATABASE_URL ="postgresql://neondb_owner:LpE2S1iVroqW@ep-noisy-tree-a5g9leg3.us-east-2.aws.neon.tech/martapi?sslmode=require"
# SQLALCHEMY_DATABASE_URL = config('SQLALCHEMY_DATABASE_URL',cast=str)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()

