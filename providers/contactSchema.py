from typing import Optional
from pydantic import BaseModel

class Contact(BaseModel):
    id: Optional[int]
    email: str
    firstname: str
    lastname: str
    phone: str
    website: Optional[str]
    status_clickup: Optional[bool] = False
    class Config: 
        orm_mode=True
