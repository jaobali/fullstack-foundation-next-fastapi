from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Define a pasta onde está o .env e passa seus valores
BASE_DIR = Path(__file__).resolve().parents[3]

class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env"
    )

settings = Settings()