# LIBRARIES
from fastapi  import APIRouter
# TYPES
from fastapi  import Depends, Request
# PROYECT
import schema
import service, middleware



# ROUTER [Private with JWT Token Auth Requirement]
routerUser = APIRouter(
    prefix="/user",
    tags=["users"],
    dependencies=[Depends(middleware.tokenJWT)]
)

@routerUser.get("/me")
async def userCurrent(r: Request):
    # Token Metadata
    token = service.token_metadata(r.headers['authorization'])
    return token













# testing endpoints
# @routerUser.get("/me")
# async def testing1():
#     return {
#         'authentication': 'worked'
#     }

# @routerUser.get("/me2")
# async def testing2(user_current: schema.User = Depends(service.token_metadata)):
#     ''' get token metadata by complex token auth middleware '''
#     return user_current

# @routerUser.get("/me3")
# async def testing3(r: Request):
#     ''' get token metadata by request object '''
#     token = r.headers['authorization']
#     # print(dir(request))
#     # for _ in ['headers', 'items', 'app', 'base_url', 'body']:
#     #     print(f'{_}:\t{getattr(request, _)}')
#     return token
