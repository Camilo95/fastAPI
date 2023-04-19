import os 
from dotenv import load_dotenv
from pathlib import Path 

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "PROYECTO-1"
    PROJECT_VERSION:str = "1.0"
    POSTGRES_LOCAL_DB:str = os.getenv('POSTGRES_LOCAL_DB') # type: ignore
    POSTGRES_LOCAL_USER:str = os.getenv('POSTGRES_LOCAL_USER') # type: ignore
    POSTGRES_LOCAL_PASSWORD:str = os.getenv('POSTGRES_LOCAL_PASSWORD') # type: ignore
    POSTGRES_LOCAL_SERVER:str = os.getenv('POSTGRES_LOCAL_SERVER') # type: ignore
    POSTGRES_LOCAL_PORT:str = os.getenv('POSTGRES_LOCAL_PORT') # type: ignore
    POSTGRES_REMOTE_DB:str = os.getenv('POSTGRES_REMOTE_DB') # type: ignore
    POSTGRES_REMOTE_USER:str = os.getenv('POSTGRES_REMOTE_USER') # type: ignore
    POSTGRES_REMOTE_PASSWORD:str = os.getenv('POSTGRES_REMOTE_PASSWORD') # type: ignore
    POSTGRES_REMOTE_SERVER:str = os.getenv('POSTGRES_REMOTE_SERVER') # type: ignore
    POSTGRES_REMOTE_PORT:str = os.getenv('POSTGRES_REMOTE_PORT') # type: ignore
    DATABASE_URL_LOCAL = f"postgresql://{POSTGRES_LOCAL_USER}:{POSTGRES_LOCAL_PASSWORD}@{POSTGRES_LOCAL_SERVER}:{POSTGRES_LOCAL_PORT}/{POSTGRES_LOCAL_DB}"
    DATABASE_URL_REMOTE = f"postgresql://{POSTGRES_REMOTE_USER}:{POSTGRES_REMOTE_PASSWORD}@{POSTGRES_REMOTE_SERVER}:{POSTGRES_REMOTE_PORT}/{POSTGRES_REMOTE_DB}"
    #CLICK UP
    TOKEN_CLICK_UP:str = os.getenv('TOKEN_CLICK_UP') # type: ignore
    LIST_ID:str = os.getenv('LIST_ID') # type: ignore
    # HUBSPOT
    HUBSPOT_ACCESS_TOKEN:str = os.getenv('HUBSPOT_ACCESS_TOKEN') # type: ignore

settings = Settings()