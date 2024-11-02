from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Date, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

db_string = "mysql+pymysql://subitouser@localhost:3306/subito"
db = create_engine(db_string, pool_recycle=3600, pool_pre_ping=True)
base = declarative_base()


class Query(base):
    __tablename__ = 'query'
    id = Column(Integer, primary_key=True)
    name = Column(Text())
    url = Column(Text())
    minPrice = Column(Integer)
    maxPrice = Column(Integer)


class Item(base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    query = relationship("Query")
    name = Column(Text())
    url = Column(Text())
    price = Column(Integer)

Session = sessionmaker(db)

base.metadata.create_all(db)
