from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base


class BaseModel(Base):
    __abstract__ = True

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                 nullable=False
                                                 )

    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                 onupdate=func.now(),
                                                 nullable=False
                                                 )
