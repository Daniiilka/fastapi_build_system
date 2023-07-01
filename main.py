from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from task_manager import TaskManager


task_manager = TaskManager('builds/tasks.yaml', 'builds/builds.yaml')

app = FastAPI()


class BuildName(BaseModel):
    build: str


@app.post("/get_tasks")
async def read_item(request: BuildName) -> List:
    result = task_manager.get_tasks_for_build(request.build)
    return result

