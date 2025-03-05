from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, database
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=database.motor)

def obtener_db():
    db = database.SesionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tareas/", response_model=schemas.Tarea)
def crear_nueva_tarea(tarea: schemas.TareaCrear, db: Session = Depends(obtener_db)):
    return crud.crear_tarea(db=db, tarea=tarea)

@app.get("/tareas/", response_model=List[schemas.Tarea])
def leer_tareas(skip: int = 0, limit: int = 100, db: Session = Depends(obtener_db)):
    return crud.obtener_tareas(db=db, skip=skip, limit=limit)

@app.get("/tareas/{tarea_id}", response_model=schemas.Tarea)
def leer_tarea(tarea_id: int, db: Session = Depends(obtener_db)):
    db_tarea = crud.obtener_tarea(db=db, tarea_id=tarea_id)
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_tarea

@app.put("/tareas/{tarea_id}", response_model=schemas.Tarea)
def actualizar_info_tarea(tarea_id: int, tarea: schemas.TareaActualizar, db: Session = Depends(obtener_db)):
    db_tarea = crud.actualizar_tarea(db=db, tarea_id=tarea_id, tarea=tarea)
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_tarea

@app.delete("/tareas/{tarea_id}", response_model=schemas.Tarea)
def eliminar_info_tarea(tarea_id: int, db: Session = Depends(obtener_db)):
    db_tarea = crud.eliminar_tarea(db=db, tarea_id=tarea_id)
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_tarea