from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel

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
    