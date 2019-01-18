from tokenize import String

from sqlalchemy import Column, Integer, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship

from app.libs.enums import PendingStatus
from app.models.base import Base


class Drift(Base):
    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    #  书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    #  请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(Integer)

    #  赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    # 枚举类型
    _pending = Column('pending', SmallInteger, Default=1)

    @property
    def pending(self):
        return PendingStatus(self._pending)

    @property.setter
    def pending(self, status):
        self._pending = status.value

    # 合理利用数据冗余记录数据历史记录
    # requester_id = Column(Integer, ForeignKey('user.id'))
    # requester = relationship('User')
    #
    # gift_id = Column(Integer)
    # gift = relationship('Gift', ForeignKey('gift.id'))
