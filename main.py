from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from task_manager import TaskManager

app = FastAPI()


class BuildName(BaseModel):
    build: str


@app.post("/get_tasks")
def read_item(request: BuildName) -> List:
    task_manager = TaskManager('builds/tasks.yaml', 'builds/builds.yaml')
    result = task_manager.get_tasks_for_build(request.build)
    return result

# todo make tests
# todo readme
