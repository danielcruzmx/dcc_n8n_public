# DESCRIPCION DE LAS PLANTILLAS N8N

## NOTA IMPORTANTE

**La comunicación entre los contenedores/servidores se da a través de las direcciones IP asignadas en la RED VIRTUAL DE DOCKER**. En el archivo ***docker-compose.yml*** estan asignadas explicitamente las direcciones IP.

Cuando usamos el navegador local para acceder a los servidores la dirección es ***localhost*** debido a que ***Docker*** establece un puente entre sus redes virtuales y la maquina huesped, el puerto es lo que hace la diferencia entre las aplicaciones.

## DESCRIPCIÓN DE LAS PLANTILLAS

- ***consulta_sql_postgres.json***

Workflow de unico nodo del tipo ***Postgres execute SQL query***, ejecuta una consulta SQL a la base de datos Postrgres. 

La configuración de la conexión debe considerar que la dirección IP del host de base de datos es ***10.13.0.2***, como se definio en el archivo ***docker-compose.yml***

- ***api_http_request.json***

Workflow de unico nodo del tipo ***HTTP Request***, hace un llamado a la API de Python para recuperar información, la dirección del servicio debe ser ***http://10.13.0.5:4557/tablaispt*** 

Para conocer los servicios que brinda la API es necesario ver su documentación en la dirección ***http://localhost:4557/docs***. Cada servicio/ruta muestra el código de llamado via ***curl***, ese código puede emplearse para configurar nodos ***HTTP Request*** (boton ***Import cURL***), solo hay que cambiar la dirección ***localhost*** por la IP de la RED VIRTUAL DE DOCKER que se le asigno al servidor API.

- ***dropdown_dinamico***

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

