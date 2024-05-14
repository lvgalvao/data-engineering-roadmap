from typing import Literal

from pydantic import PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days in minutes
    DOMAIN: str = "localhost"
    ENVIROMENT: Literal["dev", "prod"] = "dev"

    @computed_field  # type: ignore
    @property
    def server_host(self) -> str:
        if self.ENVIROMENT == "dev":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"

    if ENVIROMENT == "prod":
        POSTGRES_SCHEME: str = "postgresql+psycopg"
        POSTGRES_USER: str
        POSTGRES_PASSWORD: str
        POSTGRES_SERVER: str
        POSTGRES_PORT: int = 5432
        POSTGRES_DB: str

    @computed_field  # type: ignore
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str | PostgresDsn:
        if self.ENVIROMENT == "dev":
            return "sqlite:///database/app.db"
        return MultiHostUrl.build(
            scheme=self.POSTGRES_SCHEME,
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()  # type: ignore
