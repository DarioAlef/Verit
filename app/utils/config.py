from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    project_name: str = "Verit"
    chromadb_host: str
    groq_api_key: str
    fast_api_port: int = 5000
    compose_project_name: str = "Verit"


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
        
        
settings = Settings()