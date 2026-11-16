from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./fitterfly.db"
    meal_vision_provider: str = "mock"
    ollama_base_url: str = "http://127.0.0.1:11434"
    ollama_model: str = "qwen3-vl:2b"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
