# LIBRARIES
from fastapi        import APIRouter
# TYPES
from fastapi        import Depends
# SERVICES
import service



# ROUTER
routerUser = APIRouter(prefix="/user", tags=["users"])

# endpoints
@routerUser.get("/me", dependencies=[Depends(service.token_validation)])
async def testing():
    return {
        'authentication': 'worked'
    }
