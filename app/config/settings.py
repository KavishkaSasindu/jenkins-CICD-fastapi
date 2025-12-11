from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):
    db_host:str
    db_user:str
    db_password:str
    db_name:str
    
    def db_url(self):
        password = quote_plus(self.db_password)
        db_url = f"mysql+mysqlconnector://{self.db_user}:{password}@{self.db_host}:3306/{self.db_name}"
        return db_url
    
    class Config:
        env_file = ".env"

settings = Settings()