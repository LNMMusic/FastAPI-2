# LIBRARIES
from fastapi        import APIRouter
# TYPES
import schema
from sqlalchemy.orm import Session
from fastapi        import Depends
from fastapi        import Path, Query, Body
from typing         import List, Optional
# EXCEPTIONS
from fastapi        import HTTPException, status
# SERVICES
import service
# DB
from db.session     import get_db
# ENV
from config.env     import Env
ACCESS_TOKEN_EXPIRE = int(Env("ACCESS_TOKEN_EXPIRE"))



# ROUTER
routerAuth = APIRouter(prefix="/auth", tags=["authorization"])

# endpoints
@routerAuth.post("/signup", response_model=schema.User)
async def signup(user: schema.UserAuth, db: Session = Depends(get_db)):
    # Validation
    valid = service.valid_user_signup(user.username, db)
    if not valid:
        raise HTTPException(status_code=400, detail="Invalid SignUp - User already exist")

    # Creation
    user = service.create_user(user, db)
    return user

@routerAuth.post("/login", response_model=schema.Token)
async def login(user: schema.OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Validation
    db_user = service.get_user(user.username, db)
    valid = service.valid_user_login(db_user, user.password)
    if not valid:
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    # Authentication
    token = service.token_authorization(db_user)
    return token
