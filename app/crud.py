from sqlalchemy.orm import Session
from .models import Task


def get_task_by_id(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        return task
    return None

def update_task_name(db: Session, task_id: int, new_title: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = new_title
        db.commit()
        db.refresh(task)
        print(f"Task with id {task_id} updated to '{new_title}'.")
        return db.query(Task).filter(Task.id == task_id).first()
    print(f"Task with id {task_id} not found.")
    return None

def update_task_completed(db: Session, task_id: int, completed: bool):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = completed
        db.commit()
        db.refresh(task)
        print(f"Task with id {task_id} updated to '{completed}'.")
        return db.query(Task).filter(Task.id == task_id).first()
    print(f"Task with id {task_id} not found.")
    return None


def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        print(f"Task with id {task_id} deleted.")
        return task
    else:
        print(f"Task with id {task_id} not found.")
        return None
    
def get_tasks(db: Session, completed : bool | None = None, limit : int | None = None, offset : int | None = None, search : str | None = None):
    query = db.query(Task)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    if search is not None:
        query = query.filter(Task.title.ilike(f"%{search}%"))
    if offset is not None:
        offset = max(0, offset)  # Ensure offset is non-negative
        query = query.offset(offset)
    if limit is not None:
        if limit <= 0:
            limit = 5  # Default limit if invalid value is provided
        if limit > 100:
            limit = 100 # Maximum limit to prevent excessive data retrieval
        query = query.limit(limit)
    return query.all()