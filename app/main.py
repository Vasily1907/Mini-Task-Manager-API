from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import TaskCreate, TaskResponse
from .models import Task
from .database import SessionLocal
from . import crud
from .database import engine
from .models import Base


Base.metadata.create_all(bind=engine)



app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task


@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.get("/tasks/{task_id}")
def get_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id) 

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks_endpoint(db: Session = Depends(get_db), completed: bool | None = None, limit : int | None = None, offset : int | None = None, search : str | None = None):
    return crud.get_tasks(db, completed=completed, limit=limit, offset=offset, search=search)


@app.get("/")
def root ():
    return {"message": "Welcome to the Task API!"}


@app.put("/tasks/{task_id}")
def update_task_endpoint(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
    task = crud.update_task_name(db, task_id, task_update.title)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task

@app.put("/tasks/{task_id}/complete")
def update_task_complete_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = crud.update_task_completed(db, task_id, True)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task



