import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    # db_hostname: str
    # db_port: str
    # db_name: str
    # db_password: str

    bot_token: SecretStr

    model_config = SettingsConfigDict(
        env_file=f"{pathlib.Path(__file__).parents[2]}/.env",
        extra="ignore",
    )


settings = Settings()
