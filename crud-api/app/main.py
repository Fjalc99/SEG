from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, database, security
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/", response_model=schemas.Task)
def create_new_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tasks(db=db, skip=skip, limit=limit)

@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task_info(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(db=db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task_info(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
