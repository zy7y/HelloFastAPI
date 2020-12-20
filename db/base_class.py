from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # 自动生成表名
    @declared_attr
    def __tablename__(cls) -> str:
        # 转换成小写
        return cls.__name__.lower()
