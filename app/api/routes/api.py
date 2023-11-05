from fastapi import APIRouter

# from api.routes import predictor
from api.routes import hackathonor, predictor

router = APIRouter()
router.include_router(hackathonor.router, tags=["hackathon"], prefix="/hackathon")
router.include_router(predictor.router, tags=["predictor"], prefix="/predict")