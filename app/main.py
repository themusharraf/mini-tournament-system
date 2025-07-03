from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.db import init_db, close_db
from app.logger import logger
from app.api import router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    logger.info("Database initialized")
    try:
        yield
    finally:
        await close_db()


def create_app():
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        debug=settings.APP_DEBUG,
        lifespan=lifespan
    )

    # CORS
    allow_origins = ["http://localhost"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(router)

    return app


app = create_app()
