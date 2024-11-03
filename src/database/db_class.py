from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Date, Boolean, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# db_string = "mysql+pymysql://subitouser@localhost:3306/subito"

db_string = "mysql+pymysql://subitouser2@192.168.1.26:3306/subito"
db = create_engine(db_string, pool_recycle=3600, pool_pre_ping=True)
base = declarative_base()


class Query(base):
    __tablename__ = "query"
    id = Column(Integer, primary_key=True)
    name = Column(Text(), nullable=False)
    url = Column(Text(), nullable=False)
    minPrice = Column(Integer, nullable=True)
    maxPrice = Column(Integer, nullable=True)


class Item(base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    queryId = Column(Integer, ForeignKey("query.id"))
    title = Column(Text())
    url = Column(Text())
    price = Column(Integer)
    location = Column(Text())


Session = sessionmaker(db)

base.metadata.create_all(db)


def getQueries():
    with Session() as session:
        queries = session.query(Query).all()
        return queries

def getQuery(queryId):
    with Session() as session:
        query = session.query(Query).filter_by(id=queryId).first()
        return query


def getItems():
    with Session() as session:
        items = session.query(Item).all()
        return items


def addQuery(name, url, minPrice, maxPrice):
    with Session() as session:
        query = Query(name=name, url=url, minPrice=minPrice, maxPrice=maxPrice)
        session.add(query)
        session.commit()


def addItem(name, query, url, price):
    with Session() as session:
        item = Item(name=name, query=query, url=url, price=price)
        session.add(item)
        session.commit()

def addItem(item):
    with Session() as session:
        session.add(item)
        session.commit()


def removeQuery(queryId):
    with Session() as session:
        query = session.query(Query).filter_by(id=queryId).first()
        session.delete(query)
        session.commit()

def isPresent(item):
    with Session() as session:
        item = session.query(Item).filter_by(url=item.url).first()
        if item:
            return True
        return False