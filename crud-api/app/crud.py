from sqlalchemy.orm import Session
from app.models import Tarea
from app.schemas import TareaCrear, TareaActualizar

def crear_tarea(db: Session, tarea: TareaCrear):
    db_tarea = Tarea(titulo=tarea.titulo, descripcion=tarea.descripcion, hecha=tarea.hecha)
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def obtener_tareas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tarea).offset(skip).limit(limit).all()

def obtener_tarea(db: Session, tarea_id: int):
    return db.query(Tarea).filter(Tarea.id == tarea_id).first()

def actualizar_tarea(db: Session, tarea_id: int, tarea: TareaActualizar):
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if db_tarea:
        db_tarea.titulo = tarea.titulo
        db_tarea.descripcion = tarea.descripcion
        db_tarea.hecha = tarea.hecha
        db.commit()
        db.refresh(db_tarea)
    return db_tarea

def eliminar_tarea(db: Session, tarea_id: int):
    db_tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if db_tarea:
        db.delete(db_tarea)
        db.commit()
    return db_tarea