from sqlalchemy import Boolean, Column, Integer, JSON, Text
from providers.database import Base

class Logger(Base):
    __tablename__ = 'api_calls'
    
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    endpoint = Column(Text(), nullable=False, unique=True)
    params = Column(JSON(), nullable=False)
    result = Column(Text(), nullable=False)
