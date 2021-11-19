# LIBRARIES
from pydantic import BaseModel
from typing   import Optional, List


# USERS
# Requests
class UserBase(BaseModel):
    username: str
    email: Optional[str] = None

class UserAuth(UserBase):
    password: str

# Response
class User(UserBase):
    id: int
    is_active: Optional[bool] = None

    class Config:
        orm_mode = True