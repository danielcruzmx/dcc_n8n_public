# USO DE LA API 

En la dirección ***http://localhost:4557/docs*** se muestran las rutas de los servicios hasta ahora programados. 

Clic del raton sobre una ruta despliega la documentacion del servicio, si desea ejecutarlo presione el botón ***Try it out*** y posteriormente ***Execute***.

Es importante estar atento a la caja de texto ***curl***, esas lineas son el llamado de la API y pueden usarse para configurar nodos ***HTTP Request*** en N8N.

## NUEVOS SERVICIOS

El codigo de esta API -de momento- esta hecho para tareas de consulta de datos. 

Es muy facil incorporar nuevas rutas -nuevos servicios- relacionados con los datos de nuevas tablas de la base de datos.

Simplemente hay que seguir los pasos:

1. Defina la consulta SQL de recuperación de los datos en el archivo ***Catalogos/consultas.py***.
2. Defina el BaseModel (esquema) de los datos en el archivo ***Catalogos/esquemas.py***
3. En el archivo ***Routers/catalogos.py*** importe los objetos anteriores y agregue el codigo para la nueva ruta especificando correctamente los nuevos parametros.  
