from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.security import get_password_hash
from models.user import User
from core import deps
from schemas.user import UserCreate

router = APIRouter()

"""
1. 登录 查
2. 注册 增
3. 用户列表 查
4. 用户个人信息 查
5. 修改用户个人信息 改
"""


@router.get("/", summary="用户列表")
async def users(skip: int = 0, limit: int = 10,
                db: Session = Depends(deps.get_db),
                token: str = Depends(deps.get_current_user)
                ):
    return db.query(User).offset(skip).limit(limit).all()


@router.post("/", summary="用户新增")
async def user_add(user: UserCreate, db: Session = Depends(deps.get_db),
                   token: str = Depends(deps.get_current_user)
                   ):
    # 判断数据库是否存在
    if db.query(User).filter(User.name == user.name).first():
        raise HTTPException(
            status_code=404,
            detail="用户已存在",
        )
    user.passwd = get_password_hash(user.passwd)
    user_obj = User(**user.dict())
    db.add(user_obj)
    db.commit()
    return {"id": user_obj.id, "name": user_obj.name}


@router.delete("/{user_id}", summary="删除用户")
async def user_delete(user_id: int, db: Session = Depends(deps.get_db),
                      token: str = Depends(deps.get_current_user)):
    # 成功删除返回1，删除失败返回0
    if db.query(User).filter(User.id == user_id).delete():
        db.commit()
        return {"msg": "删除成功！"}
    return {"msg": "用户不存在"}


@router.put("/{user_id}", summary="修改用户信息")
async def user_update(user_id: int, user: UserCreate, db: Session = Depends(deps.get_db),
                      token: str = Depends(deps.get_current_user)):
    if not db.query(User).filter(User.id == user_id).update(
            {"name": user.name, "passwd": get_password_hash(user.passwd)}):
        return {"msg": "用户不存在"}
    db.commit()
    db.flush(User)
    return {"msg": "更新成功", "user": user}


@router.get("/{user_id}", summary="查询用户信息")
async def user_info(user_id: int,
                    db: Session = Depends(deps.get_db),
                    token: str = Depends(deps.get_current_user)
                    ):
    return db.query(User).filter(User.id == user_id).first()
