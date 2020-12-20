from sqlalchemy import Column, Integer, String

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True, comment="主键ID")
    name = Column(String(20), comment="名字")
    passwd = Column(String(50), comment="密码")

