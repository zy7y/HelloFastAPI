from pydantic import BaseModel


class UserBase(BaseModel):
    """用户基础模型"""
    name: str


class UserCreate(UserBase):
    """用户创建模型"""
    passwd: str



