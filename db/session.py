from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import setting

engine = create_engine(setting.SQLALCHEMY_DATABASE_URI,  connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
