import yaml
from fastapi import HTTPException
from typing import List, Dict


class TaskManager:
    def __init__(self, tasks_file: str, builds_file: str):
        self._tasks_file = tasks_file
        self._builds_file = builds_file
        self._all_tasks = None
        self._build_tasks = None
        self._read_configs()

    def _read_configs(self) -> None:
        """
        reading data from builds and tasks .yaml files
        :return: None
        """
        with open(self._tasks_file, 'r') as tasks_data, open(self._builds_file, 'r') as builds_data:
            self._all_tasks = yaml.safe_load(tasks_data)
            self._build_tasks = yaml.safe_load(builds_data)

    def _get_tasks_for_build(self, build_name: str) -> List:
        """
        get all tasks for specific build title from builds.yaml data
        :param build_name: name of specific build
        :return: list of tasks for build
        """
        for task in self._build_tasks['builds']:
            if build_name == task['name']:
                tasks_for_build = task['tasks']
                return tasks_for_build
        raise HTTPException(status_code=404, detail="No tasks found")

    def _unzip_tasks(self, tasks_queue: List, father_task: str = None, result_tasks: List = None) -> List:
        """
        a recursive method for finding dependencies for a task and queuing according to the rule that a task cannot be
        completed until all its dependencies are completed
        :param tasks_queue: list of tasks for specific build
        :param father_task: name of header task with tasks in dependencies
        :param result_tasks: list with processed tasks
        :return: list with processed tasks
        """
        if result_tasks is None:
            result_tasks = []
        processed_tasks = self._process_tasks()
        for task in tasks_queue:
            if len(processed_tasks) > 0:
                self._unzip_tasks(processed_tasks[task], task, result_tasks=result_tasks)
            elif task not in result_tasks:
                result_tasks.append(task)
        if father_task and father_task not in result_tasks:
            result_tasks.append(father_task)
        return result_tasks

    def _process_tasks(self) -> Dict:
        """
        conversion of the dictionary obtained when reading information from the tasks.yaml file. The conversion is
        necessary for more convenient work with tasks and their dependencies
        :return: dict with processed tasks {name: dependencies}
        """
        return {chunk['name']: chunk['dependencies'] for chunk in self._all_tasks['tasks']}

    def get_tasks_for_build(self, build_name: str) -> List:
        """
        it is not a private method that accumulates micromanagement for the operation of the application. Reads the
        necessary information from the configuration, collects all the necessary tasks for the build and returns a
        transformed list with the correct sequence of tasks for the build
        :param build_name: name of build from user request
        :return: list with processed tasks
        """
        tasks_for_build = self._get_tasks_for_build(build_name)
        return self._unzip_tasks(tasks_for_build)
