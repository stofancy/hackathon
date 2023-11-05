from __future__ import annotations
from pydantic import BaseModel
from typing import ClassVar, List
import random
from faker import Faker

fake = Faker()

class Task(BaseModel):
    task_id: int
    name: str
    description: str
    progress: float

    class Config:
        json_encoders = {
            float: lambda v: round(v, 2)
        }

    @staticmethod
    def generate_task_list(num_tasks=20):
        tasks = []
        for task_id in range(1, num_tasks + 1):
            task = Task(
                task_id=task_id,
                name=fake.catch_phrase(),
                description=fake.text(max_nb_chars=200, ext_word_list=None),
                progress=random.uniform(0, 1),
            )
            tasks.append(task)
        return tasks

    task_list: ClassVar[list] = []

    @staticmethod
    def tasks():
        if not Task.task_list:
            Task.task_list = Task.generate_task_list()
        return Task.task_list


class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    task_ids: List[int]

    @staticmethod
    def generate_user_list(task_list, num_users=8):
        users = []
        user_task_mapping = {}

        for user_id in range(1, num_users + 1):
            num_tasks = random.randint(2, 5)
            user = User(
                user_id=user_id,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                task_ids=[],
            )
            for _ in range(num_tasks):
                available_tasks = [
                    task for task in task_list if task.task_id not in user_task_mapping
                ]
                if not available_tasks:
                    break
                selected_task = random.choice(available_tasks)
                user.task_ids.append(selected_task.task_id)
                user_task_mapping[selected_task.task_id] = user.user_id
            users.append(user)
        return users

    user_list: ClassVar[list] = []

    @staticmethod
    def users():
        if not User.user_list:
            User.user_list = User.generate_user_list(Task.tasks())
        return User.user_list
