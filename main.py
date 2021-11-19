# LIBRARIES
import uvicorn
from fastapi import FastAPI
# CORS
from fastapi.middleware.cors import CORSMiddleware
from config.cors import origins
# ROUTER
import routes



# APP
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins.keys(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES
app.include_router(routes.routerApi)
app.include_router(routes.routerAuth)
app.include_router(routes.routerUser)

# SERVER
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
