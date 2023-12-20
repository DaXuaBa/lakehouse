from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

username = "root"
password = "134a1CA33CecB53dgg1CF4eHhAbh1Hbe"
host = "viaduct.proxy.rlwy.net"
port = "16192"
database_name = "uterace"
encoded_password = quote_plus(password)
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{username}:{encoded_password}@{host}:{port}/{database_name}"

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
