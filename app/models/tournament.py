from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, BigInteger, VARCHAR
from app.models.base import BaseModel


class Tournament(BaseModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    max_players: Mapped[int] = mapped_column(nullable=False)
    start_time: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    players: Mapped[list["Player"]] = relationship(back_populates="tournaments", cascade="all, delete-orphan")


class Player(BaseModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(255), unique=True, nullable=False)
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournaments.id"), nullable=False)

    tournament: Mapped["Tournament"] = relationship(back_populates="players")
