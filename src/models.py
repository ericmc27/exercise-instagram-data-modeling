import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = "Follower"
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_from_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('User.id'), nullable=False)


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    firstname = Column(String, unique=False, nullable=False)
    lastname = Column(String, unique=False, nullable=False)
    email = Column(String, unique=True, nullable=False)
    followers = relationship("Follower", foreign_keys=[Follower.user_to_id], backref='followed_user')
    following = relationship("Follower", foreign_keys=[Follower.user_from_id], backref='following_user')

class Comment(Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
