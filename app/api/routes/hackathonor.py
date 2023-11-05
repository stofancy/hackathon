from fastapi import APIRouter, HTTPException
from core.config import RANDOM_SEED
from models.user import User, Task
import random

router = APIRouter()

random.seed(RANDOM_SEED)


@router.get("/users")
async def users():
    try:
        return User.users()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexcepted error occurred:{str(e)}"
        )

@router.get("/tasks")
async def tasks():
    try:
        return Task.tasks()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexcepted error occurred:{str(e)}"
        )
