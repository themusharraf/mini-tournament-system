from email_validator import EmailNotValidError, validate_email
from sqlalchemy import VARCHAR, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from app.models.base import BaseModel


class Tournament(BaseModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    max_players: Mapped[int] = mapped_column(nullable=False)
    start_time: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)

    players: Mapped[list["Player"]] = relationship(back_populates="tournament", cascade="all, delete-orphan")


class Player(BaseModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(255), unique=True, nullable=False)
    tournament_id: Mapped[int] = mapped_column(ForeignKey("tournaments.id"), nullable=False)

    tournament: Mapped["Tournament"] = relationship(back_populates="players")

    @validates("email")
    def validate_email_address(self, key: str, address: str) -> str:
        """
        :param key:
        :param address:
        :return str: The validated and normalized email address.:
        :raise ValueError: If the email address is not valid.:
        """
        try:
            validate_email(address)
        except EmailNotValidError as e:
            raise ValueError(str(e))
        return address
