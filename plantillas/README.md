## Descripcion de las plantillas N8N

### NOTA IMPORTANTE

**La comunicación entre los contenedores/servidores se da a través de las direcciones IP asignadas en la RED VIRTUAL DE DOCKER**. 

Cuando usamos el navegador para acceder a los servidores la dirección es ***localhost*** debido a que ***Docker*** establece un puente entre sus redes virtuales y la maquina huesped, el puerto es lo que hace la diferencia entre las aplicaciones.

### DESCRIPCIÓN DE LAS PLANTILLAS

#### consulta_sql_postgres.json

Workflow de unico nodo del tipo ***Postgres execute SQL query***, ejecuta una consulta SQL a la base de datos Postrgres. 

La configuración de la conexión debe considerar que la dirección IP del host de base de datos es ***10.13.0.2***

#### api_http_request.json

Workflow de unico nodo del tipo ***HTTP Request***, hace un llamado a la API de Python para recuperar información, la dirección del servicio debe ser ***http://10.13.0.5:4557/tablaispt*** 

Para conocer los servicios que brinda la API es necesario ver su documentación en la dirección ***http://localhost:4557/docs***. 

Cada servicio/ruta muestra el código de llamado via ***CURL***, ese código puede emplearse para configurar nodos ***HTTP Request*** (boton ***Import cURL***), solo hay que cambiar la dirección ***localhost*** por la IP de la RED VIRTUAL DE DOCKER que se le asigno al servidor API.

#### dropdown_dinamico.json

El nodo ***Form*** de ***N8N*** permite definir con codigo JSON sus elementos, en este Workflow se usa esa modalidad.

```
[
   {
    "fieldLabel": "Equipo",
    "fieldType": "dropdown",
    "fieldOptions": {
      "values": {{ $json.values[0] }}
    },
    "requiredField": true
  }
]   
```

Los valores del combo desplegable ***dropdown*** se definen con la variable ***$json.values[0]*** no son ***valores fijos***. Esto abre la posibilidad de condicionar los valores en nodos previos.

#### GeneraCaendarioNFL.json

Este Workflow surge de la necesidad de tener en mi Calendario de Google todos los juegos de la temporada regular de la NFL. 

Calendar de Google tiene la opcion de explorar y agregar calendarios ya establecidos, existen los calendarios de cada equipo y pueden agregarse con la ayuda de las opciones nativas de Calendar, pero se tiene el inconveniente de duplicidad de eventos, además siguen siendo eventos de otros calendarios, no de mi calendario.

La solución consiste en:

1. Identificar los ID de los calendarios de los equipos
2. Elaborar una lista en Google Sheet con los nombres de los equipos y los ID de sus calendarios
3. Crear un nodo ***Google Sheet*** que lea los registros de la lista
4. Crear un nodo ***Set*** para establecer las fechas de inicio y fin de la temporada
5. Crear un nodo ***Calendar*** que recupere los eventos de los equipos en las fechas determinadas
6. Crear un nodo ***Remove Duplicates*** para eliminar eventos duplicados
7. Crear un nodo ***Set*** que asigne a cada evento un ID propio
7. Crear un nodo ***Calendar*** que genere mis eventos (partidos) con los datos previos

Una vez generado mi propio calendario de juegos, la intención es construir otro Workflow que generare cada semana la lista de encuentros y la envie a mis contactos para que hagan sus pronosticos.

#### chat_condominios.json


#### carga_leyes.json 





