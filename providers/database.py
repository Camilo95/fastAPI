from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

database_url_local = settings.DATABASE_URL_LOCAL
database_url_remote = settings.DATABASE_URL_REMOTE

engine_local = create_engine(database_url_local)
engine_remote = create_engine(database_url_remote)

# se crea la session para la serie de transaciones
Sesionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_local)

# se crea la session para la serie de transaciones
Sesionremote = sessionmaker(autocommit=False, autoflush=False, bind=engine_local)

Base = declarative_base()