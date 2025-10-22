from Routers                 import calculo
from fastapi                 import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Config.basedatos        import database

app = FastAPI(title = 'REST API')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins     = origins,
    allow_credentials = True,
    allow_methods     = ['*'],
    allow_headers     = ['*']
)

@app.on_event("startup")
async def startup():
    print('startup database')
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    print('shutdown database')
    await database.disconnect()

@app.get("/")
def hello_world():
    return {"hello": "world"}

@app.get("/items/")
async def read_items():
    return [{"elemento": "uno"}]

#app.include_router(seguridad.router)
app.include_router(calculo.router)

