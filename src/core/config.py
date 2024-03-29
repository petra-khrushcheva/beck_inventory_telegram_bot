import pathlib

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    redis_host: str
    redis_port: int
    redis_db: int

    bot_token: SecretStr

    model_config = SettingsConfigDict(
        env_file=f"{pathlib.Path(__file__).parents[2]}/.env",
        extra="ignore",
    )


settings = Settings()
