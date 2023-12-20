from backend.db.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Float
from datetime import datetime

class User(Base):
    __tablename__='USER'
    USER_ID= Column(Integer, primary_key=True, autoincrement=True)
    USER_NAME= Column(String(100)) 
    PASSWORD= Column(String(500))
    STUDENT_ID=Column(String(8))
    FULL_NAME= Column(String(100)) 
    GENDER= Column(String(50))
    ORG_NAME=Column(String(100)) 
    ORG_NAME_CHILD=Column(String(100))
    YEAR_STUDY=Column(String(100))
    CREATED_AT= Column(DateTime, default= datetime.now())
    STRAVA_ID= Column(Integer) 
    STRAVA_ACCESS_TOKEN=Column(String(200))
    STRAVA_REFRESH_TOKEN=Column(String(200))
    STRAVA_FULL_NAME =Column(String(100))
    STRAVA_IMAGE =Column(String(200))

class Run(Base):
    __tablename__='RUN'
    RUN_ID= Column(Integer, primary_key=True, autoincrement=True)
    USER_ID= Column(Integer, ForeignKey('USER.USER_ID'))
    STRAVA_RUN_ID=Column(String(50))
    NAME= Column(String(200)) 
    AVERAGE_SPEED=Column(Float)
    MAX_SPEED=Column(Float)
    AVERAGE_HEARTRATE=Column(Float)
    MAX_HEARTRATE=Column(Float)
    DISTANCE=Column(Float)
    ELAPSED_TIME=Column(String(50))
    MOVING_TIME=Column(String(50))
    TOTAL_ELEVATION_GAIN=Column(Float)
    ELEV_HIGH=Column(Float)
    TYPE=Column(String(100)) 
    CREATED_AT= Column(DateTime)
    KUDOS_COUNT= Column(String(10))
