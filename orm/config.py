from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_DB = "postgresql://usuario-ejemplo:12345@localhost:5432/bd_alumnos"
engine = create_engine(URL_DB,
                       connect_args={
                           "options": "-csearch_path=app"
                       })

SessionClass = sessionmaker(engine)

def generador_sesion():
    sesion = SessionClass()
    try:
        yield sesion
    finally:
        sesion.close()
        
BaseClass = declarative_base()        