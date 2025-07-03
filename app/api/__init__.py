from fastapi import APIRouter
from app.api.tournament import router as tournament_router

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(tournament_router)
