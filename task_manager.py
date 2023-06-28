import yaml
from typing import List, Dict


class TaskManager:
    def __init__(self, tasks_file: str, builds_file: str):
        self._tasks_file = tasks_file
        self._builds_file = builds_file
        self._all_tasks = None
        self._build_tasks = None

    def _read_configs(self) -> None:
        # todo docstring
        with open(self._tasks_file, 'r') as tasks_data, open(self._builds_file, 'r') as builds_data:
            self._all_tasks = yaml.safe_load(tasks_data)
            self._build_tasks = yaml.safe_load(builds_data)

    def _get_tasks_for_build(self, build_name: str) -> List:
        for task in self._build_tasks['builds']:
            if build_name == task['name']:
                tasks_for_build = task['tasks']
                return tasks_for_build
        # todo raise 404
        return []

    def _unzip_tasks(self, tasks_queue: List, father_task: str = None, result_tasks: List = None) -> List:
        # todo docstring
        if result_tasks is None:
            result_tasks = []
        processed_tasks = self._process_tasks()
        for task in tasks_queue:
            if len(processed_tasks) > 0:
                self._unzip_tasks(processed_tasks[task], task, result_tasks=result_tasks)
            else:
                result_tasks.append(task)
        if father_task:
            result_tasks.append(father_task)
        return result_tasks

    def _process_tasks(self) -> Dict:
        # todo docstring
        return {chunk['name']: chunk['dependencies'] for chunk in self._all_tasks['tasks']}

    def get_tasks_for_build(self, build_name: str) -> List:
        # todo docstring
        self._read_configs()
        tasks_for_build = self._get_tasks_for_build(build_name)
        return self._unzip_tasks(tasks_for_build)
