from .                  import List, status, HTTPException, APIRouter, Depends, Session
from Calculo.esquemas   import TablaIspt
from Calculo.consultas  import q_tablas_ispt
from Config.basedatos   import database

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

@router.get('/tablaispt/', response_model=List[TablaIspt], status_code = status.HTTP_200_OK)
async def read_estados(skip: int = 0, take: int = 10):
    try:
        redis_data = redis_client.get('c_tablaispt')
        if redis_data:
            return json.loads(redis_data)
        query = q_tablas_ispt
        datos =  await database.fetch_all(query)
        if not datos:
            raise HTTPException(status_code = 404, detail = "No hay datos para la consulta")
        content = datadb_to_json(datos, TablaIspt)
        redis_client.setex('c_tablaispt', 86400, json.dumps(content, default=str))        
        return datos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

