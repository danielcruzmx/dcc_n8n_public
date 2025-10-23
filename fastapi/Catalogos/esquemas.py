from . import BaseModel, date, Optional

class TablaIspt(BaseModel):
   tipo_tabla:  str
   limite_inferior: float
   limite_superior: float
   bruto: float
   cuota_fija: float
   excedente: float
