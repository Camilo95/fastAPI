from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from providers.database import Base

class Contact(Base):
    __tablename__ = 'Contact'
    
    id = Column(Integer, primary_key=True, index=True , autoincrement=True)
    email = Column(String(150), nullable=False, unique=True)
    firstname = Column(String(200), nullable=False)
    lastname = Column(String(200), nullable=False)
    phone = Column(String(18), nullable=False)
    website = Column(String(200))
    status_clickup = Column(Boolean, default=False)
