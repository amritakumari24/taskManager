from fastapi import APIRouter
task_routes = APIRouter(prefix="/tasks")

from src.tasks import controller

@task_routes.post("/create")
def create_task():
    return controller.create_task()


