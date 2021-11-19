# LIBRARIES
from pydantic import BaseModel
from typing   import Optional, List


# TOKEN
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None


# LOGIN
from fastapi.security import OAuth2PasswordRequestForm
''' Token Generator to oauth2 login type for user
    
    OAuth2PasswordRequestForm is a class dependency that declares a form body with:
    =>  The username
    =>  The password
    =>  An optional scope field as a big string, composed of strings separated by spaces
    =>  An optional grant_type
'''