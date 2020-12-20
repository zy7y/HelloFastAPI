from datetime import timedelta, datetime

from jose import jwt
from passlib.context import CryptContext

from core.config import setting

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 生成token
def create_access_token(
        subject: str, expires_delta: timedelta = None
) -> str:
    """
    使用python-jose库生成用户token
    :param subject: 一般传递一个用户id
    :param expires_delta: 有效时间
    :return: 加密后的token字符串
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证用户输入密码与加密过后的密码是否相等，使用passlib库完成
    :param plain_password: 用户输入的明文密码
    :param hashed_password: hash加密过后的密码
    :return: 是否相等
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    将用户输入的明文密码，使用hash算法加密,每次加密的算法都不一样
    :param password: 明文密码
    :return: 加密过后的密码
    """
    return pwd_context.hash(password)


# Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDg0NTcwNDcsInN1YiI6Ijxtb2RlbHMudXNlci5Vc2VyIG9iamVjdCBhdCAweDAwMDAwMUMyQUQ5OENEMzA-In0.MUGpTbLiyR_FacOp7zB5PCgz-C3TSpenDUS9CSonj2w
# Authorization
# http://127.0.0.1:8000/token