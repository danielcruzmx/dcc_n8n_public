import requests
import pandas   as pd

def obt_data(msg, ruta, api):
    response = None
    url_env  = api + ruta
    response = requests.get(url_env)
    if not response:
        print("No hay registros para {msg} en la ruta {ruta}.".format(msg = msg, ruta = url_env))
    return response

def carga_tabla_ispt(api):
    tablaIspt = obt_data("tabla ispt", "/tablaispt/", api)    
    if tablaIspt.status_code == 200:
        dfTbi = pd.json_normalize(tablaIspt.json())
        return dfTbi
    else:
        return None

def ispt(tabla_ispt, monto):
    if not tabla_ispt.empty:
        ran = tabla_ispt[(tabla_ispt.limite_inferior <= monto) & 
                         (tabla_ispt.limite_superior >= monto) & 
                         (tabla_ispt.tipo_tabla == '80')]
        val = ran.to_dict('records')
        res = ( monto  - val[0]['limite_inferior']) * (val[0]['excedente'] /  100.0) + val[0]['cuota_fija'] 
        return res 
    else:
        return 0.0
