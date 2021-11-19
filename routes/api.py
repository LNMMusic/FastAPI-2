# LIBRARIES
from fastapi import APIRouter



# ROUTER [Public - Not TokenJWT Middleware neccessary]
routerApi = APIRouter(
    prefix="/api",
    tags=["api"]
)

# endpoints
@routerApi.get("/home")
async def home():
    return {
        'Welcome': 'This is the Home of the API'
    }