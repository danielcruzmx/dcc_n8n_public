# DESCRIPCION DE LAS PLANTILLAS

## consulta_sql_postgres.json

Workflow de unico nodo del tipo **Postgres execute SQL query** que muestra como hacer una consulta SQL a la base de datos. La configuración de la conexión debe considerar que la dirección IP del host de base de datos es 10.13.0.2, asi se definio en la **RED VIRTUAL DE DOCKER** en el docker-compose.yml

**La comunicacion entre los contenedores se da a través de las direcciones IP asignadas en la RED VIRTUAL DE DOCKER.** Pero cuando usamos el navegador local para acceder a los contenedores se usa ***localhost*** debido a que **Docker** establece un puente entre sus redes virtuales y la maquina huesped, el puerto es lo que hace la diferencia entre las aplicaciones.

## api_http_request.json

Workflow de Unico nodo del tipo **HTTP Request** que ilustra el llamado a la API desarrollada en Python, el servicio requerido esta en la dirección http://10.13.0.5:4557/tablaispt. 

El servidor API de Python presenta la documentacion de sus servicios en http://localhost:4557/docs, ahi se ilustra el llamado a la API con la sentencia ***curl***, podemos copiar dicha sentencia y usarla para configurar el nodo con la ayuda del boton **Import cURL**. Solo hay que cambiar el ***localhost*** por la IP de la RED VIRTUAL que se le asigno al servidor API.