from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from api import user, movie, login
from core.logger import logger
from core.config import setting

app = FastAPI(
    title=setting.TITLE,
    docs_url=setting.DOCS_URL,
    description=setting.DESCRIPTION,
    version=setting.VERSION,
)

# 设置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=setting.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 自定义访问日志中间件
@app.middleware("http")
async def logger_request(request: Request, call_next):
    # https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
    logger.info(f"访问记录:{request.method} url:{request.url}\nheaders:{request.headers.get('user-agent')}"
                f"\nIP:{request.client.host}")
    response = await call_next(request)
    return response

# 将子路由注册到APP
app.include_router(router=login.router, tags=["登录"])
app.include_router(router=user.router, prefix="/users", tags=["user"])
app.include_router(router=movie.router, prefix="/movies", tags=["movie"])


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", port=5555, reload=True, debug=True)
