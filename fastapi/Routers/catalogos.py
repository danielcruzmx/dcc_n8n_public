from .                   import List, status, HTTPException, APIRouter, Depends, Session
from Catalogos.esquemas  import TablaIspt
from Catalogos.consultas import q_tablas_ispt
from Config.basedatos    import database

import json
import redis
import os

cache  = os.getenv("CACHE")
router = APIRouter()
redis_client = redis.Redis(host=cache, port='6379', password= '', db = 0)

def datadb_to_json(datadb, basemodel):
    dicc = {}
    for k in basemodel.__fields__:
        dicc[k] = k
    content = []
    for dato in datadb:
        item = {}
        for k in dicc:
            item[k] = dato[dicc[k]]
        content.append(item)        
    return content

async def get_data(redis_key, esquema, consulta):
    redis_data = redis_client.get(redis_key)
    if redis_data:
        return json.loads(redis_data)
    datos =  await database.fetch_all(consulta)
    if not datos:
        raise HTTPException(status_code = 404, detail = "No hay datos para la consulta")
    content = datadb_to_json(datos, esquema)
    redis_client.setex(redis_key, 86400, json.dumps(content, default=str))        
    return datos

@router.get('/tablaispt/', response_model=List[TablaIspt], status_code = status.HTTP_200_OK)
async def read_ispt(skip: int = 0, take: int = 10):
    try:
        data = await get_data('c_tablaispt', TablaIspt, q_tablas_ispt)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
