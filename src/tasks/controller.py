from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

def create_task(body: TaskSchema, db: Session):
    new_task = TaskModel(**body.model_dump())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {
        "status": "task created successfully!",
        "data": {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "is_completed": new_task.is_completed,
        },
    }

def get_tasks(db:Session ):
    tasks = db.query(TaskModel).all()
    return {"status": "all tasks", "data": tasks}


def get_one_task(task_id:int,db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="task id is incoorect")
    return {"status": "task fetched successfully", "data": one_task}


def update_task( body:TaskSchema,task_id:int, db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="task id is incoorect")
    body = body.model_dump()
    for field , value in body.items():
        setattr(one_task, field, value)
    

    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return {
            "status": "task updated successfully!",
            "data": {
                "id": one_task.id,
                "title": one_task.title,
                "description": one_task.description,
                "is_completed": one_task.is_completed,
            },
        }



def delete_task(task_id: int, db: Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="task id is incoorect")

    db.delete(one_task)
    db.commit()
    return  None