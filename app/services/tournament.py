from datetime import timedelta

from fastapi import HTTPException, status
from sqlalchemy import func, select

from app.dependencies.database import DBSession
from app.models import Player, Tournament
from app.schemas.tournament import (
    PlayerCreate,
    PlayerRead,
    TournamentCreate,
    TournamentRead,
)


async def tournament_create(db: DBSession, tournament: TournamentCreate) -> TournamentRead:
    result = await db.execute(
        select(Tournament).where(
            Tournament.name == tournament.name,
            Tournament.start_time == tournament.start_time,
        )
    )
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tournament with this name and start time already exists",
        )

    time_window_start = tournament.start_time - timedelta(hours=1)
    time_window_end = tournament.start_time + timedelta(hours=1)

    overlapping = await db.execute(
        select(Tournament).where(Tournament.start_time.between(time_window_start, time_window_end))
    )
    if overlapping.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Another tournament is scheduled within 1 hour of this time",
        )
    new_tournament = Tournament(
        name=tournament.name,
        max_players=tournament.max_players,
        start_time=tournament.start_time,
    )
    db.add(new_tournament)
    await db.commit()
    await db.refresh(new_tournament)

    return TournamentRead.model_validate(new_tournament)


async def register_player(db: DBSession, tournament_id: int, player_data: PlayerCreate) -> PlayerRead:
    result = await db.execute(select(Tournament).where(Tournament.id == tournament_id))
    tournament = result.scalar_one_or_none()
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    count_result = await db.execute(
        select(func.count()).select_from(Player).where(Player.tournament_id == tournament_id)
    )
    player_count = count_result.scalar()

    if player_count is not None and tournament.max_players is not None:
        if player_count >= tournament.max_players:
            raise HTTPException(status_code=400, detail="Tournament is full")
    email_check = await db.execute(
        select(Player).where(Player.email == player_data.email, Player.tournament_id == tournament_id)
    )

    if email_check.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email already registered in this tournament")
    new_player = Player(
        name=player_data.name,
        email=player_data.email,
        tournament_id=tournament_id,
    )
    db.add(new_player)
    await db.commit()
    await db.refresh(new_player)

    return PlayerRead.model_validate(new_player)


async def get_players_by_tournament(
    db: DBSession,
    tournament_id: int,
) -> list[PlayerRead]:
    players_query = await db.execute(select(Player).where(Player.tournament_id == tournament_id))
    players = players_query.scalars().all()

    if not players:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No players found for this tournament",
        )

    return [PlayerRead.model_validate(p) for p in players]
