from pydantic import BaseModel


class MovieCreate(BaseModel):
    """电影模型基类"""
    title: str
    year: str
