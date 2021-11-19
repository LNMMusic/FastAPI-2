# LIBRARIES
from fastapi        import APIRouter
# TYPES
from fastapi        import Depends
# Proyect
import service
import middleware



# ROUTER
routerUser = APIRouter(prefix="/user", tags=["users"])

# endpoints
@routerUser.get("/me", dependencies=[Depends(service.token_validation)])
async def testing():
    return {
        'authentication': 'worked'
    }

@routerUser.get("/me2", dependencies=[Depends(middleware.tokenJWT)])
async def testing():
    return {
        'authentication': 'worked'
    }
