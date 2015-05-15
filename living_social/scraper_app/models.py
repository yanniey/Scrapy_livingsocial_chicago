# use SQLalchemy to connect to Postgres DB

# 1. define a function to connect to database

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.engine.url import URL
# URL must be uppercase!!!
from sqlalchemy.ext.declarative import declarative_base 
# to map a class that defines our table structure to Postgres

import settings

DeclarativeBase = declarative_base()

def db_connect():
	"use settings.py to connect to database. return sqlalchemy engine instance "
	return create_engine(URL(**settings.DATABASE)) 
# the `**` unpacks all the values within the DATABASE dictionary (defined in `settings.py`). The `URL` function maps keys and values to a URL 

def create_deals_table(engine):
	DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
	"sqlalchemy deals model "
	__tablename__ = "deals"

	id = Column(Integer,primary_key=True)
	title = Column('title', String)
	link = Column('link', String, nullable = True) 
	# nullable : it's okay to leave blank
	location = Column('location', String, nullable = True)
	original_price = Column('original_price', Integer, nullable = True)
	price = Column('price', Integer, nullable = True)
	end_date = Column('end_date', DateTime, nullable = True) 
	# each field will be mapped to a column in our table through `create_deals_table()`