# SECURITY
from fastapi.security import OAuth2PasswordBearer;    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
from jose             import JWTError, jwt
from datetime         import datetime, timedelta
# ENV
from config.env       import Env                      SECRET_KEY = Env("SECRET_KEY");ALGORITHM  = Env("ALGORITHM")
# TYPES
from fastapi          import Depends
from typing           import List, Optional
import model, schema
# DB
from db.session       import get_db
# EXCEPTIONS
from fastapi          import HTTPException, status
credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Could not validate credentials",
                        headers={"WWW-Authenticate": "Bearer"})



# AUTH Token
def token_authorization(db_user: model.User, expires_delta: Optional[timedelta] = None) -> schema.Token:
    # Expiration
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    # Metadata
    user = schema.User.from_orm(db_user)
    data = user.dict()
    data.update({'exp': expire})

    # Creation
    token= jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return schema.Token(
        access_token=token,
        token_type="Bearer"
    )


def token_validation(db: Session = Depends(get_db), token:str = Depends(oauth2_scheme)) -> None:
    ''' Raise an error if Token is Invalid '''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        
        db_user= db.query(models.User).get(payload["id"])
        if db_user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception


def token_metadata(db: Session = Depends(get_db), token:str = Depends(oauth2_scheme)) -> schema.User.from_orm:
    ''' Raise an error if Token is Invalid and Returns Token Metadata '''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        
        db_user= db.query(models.User).get(payload["id"])
        if db_user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    return schema.User.from_orm(db_user)