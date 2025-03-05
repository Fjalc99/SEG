from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_BASE_DATOS_SQLALCHEMY = "sqlite:///./test.db"

motor = create_engine(URL_BASE_DATOS_SQLALCHEMY, connect_args={"check_same_thread": False})
SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor)
Base = declarative_base()

def obtener_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()