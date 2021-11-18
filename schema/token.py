# LIBRARIES
from pydantic import BaseModel
from typing   import Optional, List


# TOKEN
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
