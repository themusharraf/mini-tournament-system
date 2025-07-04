from fastapi import APIRouter

from app.dependencies.database import DBSession
from app.schemas.base import BaseResponse
from app.schemas.tournament import PlayerCreate, TournamentCreate
from app.services.tournament import (
    get_players_by_tournament,
    register_player,
    tournament_create,
)

router = APIRouter(prefix="/tournaments", tags=["Tournament"])


@router.post("", response_model=BaseResponse)
async def create_tournament(tournament: TournamentCreate, db: DBSession) -> BaseResponse:
    tournament_resp = await tournament_create(db, tournament)
    return BaseResponse(data=tournament_resp)


@router.post("/{tournament_id}/register", response_model=BaseResponse)
async def register_tournament(tournament_id: int, player: PlayerCreate, db: DBSession) -> BaseResponse:
    result = await register_player(db, tournament_id, player)
    return BaseResponse(data=result)


@router.get("/{tournament_id}/players", response_model=BaseResponse)
async def list_players(tournament_id: int, db: DBSession) -> BaseResponse:
    players = await get_players_by_tournament(db, tournament_id)
    return BaseResponse(data=players)
