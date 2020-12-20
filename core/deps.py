# 依赖项文件
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer


from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from core.config import setting
from db.session import SessionLocal
from models.user import User

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)


def get_db():
    """
    用于接口中的数据库-依赖项，每个接口依赖此接口 会进行查询接口执行完毕自动关闭该实例
    :return: 数据库的实例对象
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# 获取当前用户
def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
):
    print(token)
    try:
        payload = jwt.decode(
            token, setting.SECRET_KEY, algorithms=[setting.ALGORITHM]
        )
    except (jwt.JWTError, ValidationError, AttributeError):
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    user_id = payload["sub"]
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=403, detail="用户不存在")
    return {"id": user.id, "name": user.name}
