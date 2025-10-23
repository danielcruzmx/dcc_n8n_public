# PRUEBA DE LA API 

Despues de arrancar el contenedor *FastApi* puede entrar a el en la dirección *http://localhost:4557/docs*, se muestran las rutas de los servicios programados. De clic sobre la ruta para desplegar la documentacion del servicio y si desea ejecutarlo presione el botón *Try it out* y posteriormente *Execute*.

Es importante estar atento a la caja de texto *curl*, esas lineas son el llamado de la API y pueden usarse para configurar nodos *HTTP Request* de N8N.

## CREACION DE NUEVOS SERVICIOS

El codigo de esta API -de momento- esta hecho para tareas de consulta de datos. Es muy facil incorporar rutas -nuevos servicios- relacionados con nuevas tablas que se creen en la base de datos.

Debe seguir los pasos:

1. Definir la consulta SQL de recuperación de los datos (Catalogos/consultas.py).
2. Definir el BaseModel (esquema) de los datos (Catalogos/esquemas.py).
3. Importar lo anterior al programa donde estan las rutas (Routers/catalogos.py), agregue el codigo de la ruta *@router.get*, especificando correctamente los nuevos parametros.  
