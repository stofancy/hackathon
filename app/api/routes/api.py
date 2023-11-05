from fastapi import APIRouter, Request

# from api.routes import predictor
from api.routes import hackathonor

router = APIRouter()
router.include_router(hackathonor.router, tags=["hackathon"], prefix="/hackathon")