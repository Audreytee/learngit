"""
 Created by yan on 2018/8/30 17:00
"""
__author__ = 'yan'

# flask 的很多东西都是复用和封装，werzeug,只提供最核心的功能

# sqlalchemy
# flask_sqlalchemy
# wtforms
# flask_wtforms
# werkzeug the 3rd route lib

from sqlalchemy import Column,Integer,String
from app.models.base import db,Base


class Book(Base):
    """
       一些属性定义重复性比较大，元类可以解决这个问题
    """
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)  # nullable 不允许为空
    _author = Column('author', String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)  # unique，isbn必须唯一，不能重复
    summary = Column(String(1000))
    image = Column(String(50))
