from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from .database import Base

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, index = True)
    body = Column(String, index = True) 
    publisched = Column(Boolean, default = False)
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
