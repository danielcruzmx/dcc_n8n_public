import databases
import sqlalchemy
import os

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

db_username = os.getenv("USERDB")
db_password = os.getenv("PASSDB")
host        = os.getenv("HOSTDB")
port        = os.getenv("PORTDB")
db          = os.getenv("DATABASE")
ssl_mode    = 'prefer'


DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host, port, db, ssl_mode)

#print(DATABASE_URL)

database = databases.Database(DATABASE_URL)

engine   = sqlalchemy.create_engine(
    DATABASE_URL, pool_size = 3, max_overflow = 0
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

metadata = sqlalchemy.MetaData()
metadata.create_all(engine)

