from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host:str
    db_user:str
    db_password:str
    db_name:str
    
    def db_url(self):
        db_url = f"mysql+mysqldb://{self.db_user}:{self.db_password}@{self.db_host}:3306/{self.db_name}"
        return db_url
    
    class Config:
        env_file = ".env"

settings = Settings()