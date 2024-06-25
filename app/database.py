from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from dotenv import load_dotenv
import os
load_dotenv()


conn_db = os.getenv['DATABASE_URL']


DATABASE_URL = conn_db


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()