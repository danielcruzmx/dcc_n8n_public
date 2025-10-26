## Uso de la API REST de Python

### DOCUMENTACION

En la dirección ***http://localhost:4557/docs*** se muestra la documentación de los servicios programados, clic del raton sobre una ruta especifica despliega mayor información.

- Parametros requeridos por el servicio, nombre y tipo
- Botones para la ejecución del servicio ***Try it out*** y posteriormente ***Execute***.
- Area de respuesta, codigo, tipo de respuesta y resultado.
- Sentencia ***curl*** de llamado

Es importante estar atento a la caja de texto ***curl***, esas lineas se usan para configurar nodos ***HTTP Request*** en N8N.

### CREACIÓN DE NUEVOS SERVICIOS

El codigo de esta API -de momento- esta hecho para tareas de consulta de datos. 

Es muy facil incorporar nuevas rutas -nuevos servicios- relacionados con los datos de nuevas tablas de la base de datos.

Simplemente hay que seguir los pasos:

1. Define la consulta SQL de recuperación de los datos en el archivo ***Catalogos/consultas.py***.
2. Define el BaseModel (esquema) de la respuesta SQL en el archivo ***Catalogos/esquemas.py***
3. Importa los objetos en el archivo ***Routers/catalogos.py*** y agrega el codigo para la nueva ruta tomando como base una ruta ya definida y en funcionamiento.

### CACHE

Cuando se llama a un servicio por primera vez la API ejecuta la sentencia SQL para recuperar los datos desde PostgreSql y los almacena en la instancia de ***REDIS*** con una llave de acceso. Para llamados posteriores la API recupera los datos de la instancia de ***REDIS***.

Es importante señalar que la definicion de la llave de acceso en ***REDIS*** tiene tiempo de vencimiento en segundos, esto significa que en algun momento la recuperación de los datos se hará nuevamente de la base de datos.

En teoria la recuperación de datos debe ser mas rapida del cache ***REDIS***. 

Se recomienda usar este mecanismo en tablas que no cambian sus datos constantemente, los catálogos por ejemplo.


