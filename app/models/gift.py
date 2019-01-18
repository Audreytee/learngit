from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, SmallInteger, desc, func
from app.models.base import db, Base
from sqlalchemy.orm import relationship

from app.spider.yushu_book import YuShuBook
from collections import namedtuple

EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))

    # 礼物是否赠送成功
    launched = Column(Boolean, default=False)

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.models.wish import Wish
        # 根据传入的isbn,到wish表中计算出某个礼物的wish心愿数量
        # 条件表达式,sql in 查询
        # 跨模型的方式使用这种方式
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
                                                                             Wish.isbn.in_(isbn_list),
                                                                             Wish.status == 1).group_by(
            Wish.isbn).all()
        # 字典的方式
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 类代表礼物这个事务,它是抽象,不是具体的'一个',特征+行为
    @classmethod
    def recent(cls):
        # 链式调用
        # 主体 Query
        # 子函数
        # first(),all()最终生成sql语句
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift

    # 返回对象的方式
    # @classmethod
    # def get_wish_counts(cls, isbn_list):
    #     # 根据传入的isbn,到wish表中计算出某个礼物的wish心愿数量
    #     # 条件表达式,sql in 查询
    #     count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
    #                                                                          Wish.isbn.in_(isbn_list),
    #                                                                          Wish.status == 1).group_by(
    #         Wish.isbn).all()
    #     count_list = [EachGiftWishCount(w[0], w[1]) for w in count_list]
    #     return count_list
