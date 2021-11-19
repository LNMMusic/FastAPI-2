# LIBRARIES
from fastapi import APIRouter
# TYPES
from fastapi import Depends
from fastapi import Path, Query, Body
from typing  import List, Optional
import schema
# SERVICES
import service


# Router
routerAuth = APIRouter(prefix="/auth", tags=["authorization"])


# endpoints
@endpoint.post("/signup", response_model=schema.User)
async def signup(user: schema.UserCreate):
    db_user = service.create_user(user)
    if db_user.id == 0:
        raise HTTPException(status_code=400, detail="Username already registered")
    return db_user

async def login():
    pass

async def logout():
    pass