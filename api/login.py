from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core import deps
from core.security import verify_password, create_access_token
from models.user import User

router = APIRouter()


class OAuth2Form(OAuth2PasswordRequestForm):
    """将登录使用的表单中部分字段隐藏, 使用该模型将无法使用swaager登录"""
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


@router.post("/login", summary="用户登录")
async def login(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    # 判断用户是否存在
    user = db.query(User).filter(User.name == form_data.username).first()
    if not user or not verify_password(form_data.password, user.passwd):
        raise HTTPException(status_code=404, detail="用户名或密码错误")
    # 如果使用的模行不包含"token_type": "bearer", "access_token": token swaggger ui中将出现token undefined
    return {"id": user.id, "name": user.name, "token_type": "bearer", "access_token": create_access_token(user.id)}


