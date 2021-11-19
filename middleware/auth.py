# SECURITY
from fastapi.security import OAuth2PasswordBearer
# TYPES
from fastapi          import Depends


# Middleware Token Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def tokenJWT(token: str = Depends(oauth2_scheme)):
    pass