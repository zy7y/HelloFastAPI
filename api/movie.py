from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import deps
from models.movie import Movie
from schemas.movie import MovieCreate

router = APIRouter()


@router.get("/", summary="查询所有电影")
async def movies(skip: int = 0, limit: int = 10,
                 db: Session = Depends(deps.get_db),
                 token: str = Depends(deps.get_current_user)
                 ):
    return db.query(Movie).offset(skip).limit(limit).all()


@router.post("/", summary="新增电影记录")
async def movie_add(movie: MovieCreate, db: Session = Depends(deps.get_db),
                    token: str = Depends(deps.get_current_user)
                    ):
    if db.query(Movie).filter(Movie.title == movie.title).first():
        return {"msg": "该电影已存在"}
    movie_db = Movie(**movie.dict())
    db.add(movie_db)
    db.commit()
    return {"id": movie_db.id, "name": movie_db.title, "year": movie_db.year}


@router.delete("/{movie_id}", summary="删除电影信息")
async def movie_delete(movie_id: int, db: Session = Depends(deps.get_db),
                       token: str = Depends(deps.get_current_user)
                       ):
    if db.query(Movie).filter(Movie.id == movie_id).delete():
        return {"msg": "删除成功"}
    return {"msg": "id不存在"}


@router.get("/{movie_id}", summary="查询电影信息")
async def movie_info(movie_id: int, db: Session = Depends(deps.get_db),
                     token: str = Depends(deps.get_current_user)
                     ):
    return db.query(Movie).filter(Movie.id == movie_id).first()


@router.put("{movie_id}", summary="修改信息")
async def movie_update(movie_id: int, movie: MovieCreate,
                       db: Session = Depends(deps.get_db),
                       token: str = Depends(deps.get_current_user)
                       ):
    data = {
        Movie.title: movie.title,
        Movie.year: movie.year
    }
    if db.query(Movie).filter(Movie.id == movie_id).update(data):
        db.commit()
        db.flush(Movie)
        return {"msg": "修改成功", "id": movie_id, "info": movie}
    return {"msg": "id不存在"}

