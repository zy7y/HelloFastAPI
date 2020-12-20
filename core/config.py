import secrets
from typing import List

from pydantic import BaseSettings


class SettingsI(BaseSettings):
    """配置类"""
    # 文档设置
    TITLE: str = "Hello FastAPI-接口文档"
    DOCS_URL: str = "/docs"
    DESCRIPTION: str = """
    **仿照Hello Flask 实战项目设计的后端API http://helloflask.com/tutorial/**
    > 目的是学习FastAPI... ; 初始账号密码： root | 123456
    - 作者： zy7y
    - Blog: https://www.cnblogs.com/zy7y
    - Github: https://github.com/zy7y
    """
    VERSION: str = "6.6.6"

    # token相关
    ALGORITHM: str = "HS256"  # 加密算法
    SECRET_KEY: str = secrets.token_urlsafe(32)  # 随机生成的base64位字符串
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # token的时效 3 天 = 60 * 24 * 3

    # 跨域设置
    CORS_ORIGINS: List[str] = ["*", ]

    # 数据库url配置
    SQLALCHEMY_DATABASE_URI: str = r"sqlite:///F:\coding\watchlist\watchlist.db"


setting = SettingsI()
