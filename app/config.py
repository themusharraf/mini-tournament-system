from pydantic_settings import BaseSettings


class Config(BaseSettings):
    APP_NAME: str = "Tournaments API"
    APP_AUTHOR: str = "Musharraf DEV"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "Manage Tournaments and Player Registration API"
    APP_DEBUG: bool = False

    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@" f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Config()  # type: ignore
