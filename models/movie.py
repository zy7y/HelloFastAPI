from sqlalchemy import Column, Integer, String

from db.base_class import Base


class Movie(Base):
    id = Column(Integer, primary_key=True, index=True, comment="主键")
    title = Column(String(60), comment="标题")
    year = Column(String(4), comment="电影年份")
