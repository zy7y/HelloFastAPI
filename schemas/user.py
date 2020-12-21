from pydantic import BaseModel


class UserBase(BaseModel):
    """用户输入基础模型"""
    name: str


class UserCreate(UserBase):
    """用户输入创建模型"""
    passwd: str


class UserUpdate(UserBase):
    """用户输入更新模型"""
    pass


class UserDB(UserBase):
    """数据库的基础模型"""
    id: int = None

    class Config:
        """兼容orm模型"""
        orm_mode = True
