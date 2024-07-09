import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    name = Column(String(50), nullable=False) #permito valores null?
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    posts = relationship("Post", backref="posts")
    likes = relationship("Like", backref="likes")
    messages = relationship("Message", backref="messages")
    followed = relationship("Followed", backref="followed")

class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(500))
    
    user_id = Column(Integer, ForeignKey("user.id"))

class Like(Base):
    __tablename__ = "Like"
    id = Column(Integer, primary_key=True)
    is_liked = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("user.id"))

class Message(Base):
    __tablename__ = "Message"
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("user.id"))    

class Followed(Base):
    __tablename__ = "Follow"
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey("user.id"))
    followed_id = Column(Integer, ForeignKey("user.id"))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
