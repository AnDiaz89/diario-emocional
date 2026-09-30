from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuracion de la app, leida desde el archivo .env"""
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()