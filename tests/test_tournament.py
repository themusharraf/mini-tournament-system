from datetime import datetime, timedelta

import pytest

from app.schemas.tournament import PlayerCreate, TournamentCreate
from app.services.tournament import (
    get_players_by_tournament,
    register_player,
    tournament_create,
)


@pytest.mark.asyncio
async def test_create_tournament_success(db_session):
    tournament = TournamentCreate(name="Chess Cup", max_players=10, start_time=datetime(2025, 7, 5, 13, 0, 0))
    result = await tournament_create(db_session, tournament)
    assert result.name == tournament.name
    assert result.max_players == tournament.max_players


@pytest.mark.asyncio
async def test_create_tournament_duplicate(db_session):
    tournament = TournamentCreate(
        name="Duplicate Cup",
        max_players=10,
        start_time=datetime.now() + timedelta(days=2),
    )
    await tournament_create(db_session, tournament)

    with pytest.raises(Exception) as exc:
        await tournament_create(db_session, tournament)
    assert "already exists" in str(exc.value)


@pytest.mark.asyncio
async def test_register_player_success(db_session):
    tournament = TournamentCreate(
        name="Register Test",
        max_players=5,
        start_time=datetime.now() + timedelta(days=3),
    )
    t = await tournament_create(db_session, tournament)
    player = PlayerCreate(name="Alice", email="alice@gmail.com")
    result = await register_player(db_session, tournament_id=t.id, player_data=player)
    assert result.name == "Alice"
    assert result.email == "alice@gmail.com"


@pytest.mark.asyncio
async def test_register_same_email_twice(db_session):
    tournament = TournamentCreate(
        name="Email Check",
        max_players=5,
        start_time=datetime.now() + timedelta(days=4),
    )
    t = await tournament_create(db_session, tournament)

    player = PlayerCreate(name="Bob", email="bob@gmail.com")
    await register_player(db_session, tournament_id=t.id, player_data=player)

    with pytest.raises(Exception) as exc:
        await register_player(db_session, tournament_id=t.id, player_data=player)
    assert "already registered" in str(exc.value)


@pytest.mark.asyncio
async def test_get_players_by_tournament(db_session):
    tournament = TournamentCreate(
        name="Player List",
        max_players=5,  # Changed from 3 to 5 to meet validation requirements
        start_time=datetime.now() + timedelta(days=5),
    )
    t = await tournament_create(db_session, tournament)

    await register_player(db_session, t.id, PlayerCreate(name="Tom", email="tom@gmail.com"))
    await register_player(db_session, t.id, PlayerCreate(name="Jerry", email="jerry@gmail.com"))

    players = await get_players_by_tournament(db_session, t.id)
    assert len(players) == 2
    player_names = [p.name for p in players]
    assert "Tom" in player_names
    assert "Jerry" in player_names
