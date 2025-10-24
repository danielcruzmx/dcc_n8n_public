# DESCRIPCION DE LAS PLANTILLAS N8N

## NOTA IMPORTANTE

**La comunicacion entre los contenedores/servidores se da a través de las direcciones IP asignadas en la RED VIRTUAL DE DOCKER** en el archivo ***docker-compose.yml***.

Cuando usamos el navegador local para acceder a los servidores se usa ***localhost*** debido a que ***Docker*** establece un puente entre sus redes virtuales y la maquina huesped, el puerto es lo que hace la diferencia entre las aplicaciones.

### consulta_sql_postgres.json

Workflow de unico nodo del tipo ***Postgres execute SQL query***, ejecuta una consulta SQL a la base de datos Postrgres. 

La configuración de la conexión debe considerar que la dirección IP del host de base de datos es ***10.13.0.2***, como se definio en el archivo ***docker-compose.yml***

### api_http_request.json

Workflow de unico nodo del tipo ***HTTP Request*** que hace el llamado a la API desarrollada en Python para traer información, el servicio requerido esta en la dirección ***http://10.13.0.5:4557/tablaispt*** 

La documentacion de los servicios del servidor API esta en la dirección ***http://localhost:4557/docs***, ahi se muestra el llamado a la API con la sentencia ***curl***, podemos copiar dicha sentencia y usarla para configurar el nodo ***HTTP Request*** con la ayuda del boton ***Import cURL***. Solo hay que asegurarse de  cambiar el ***localhost*** por la IP de la RED VIRTUAL DE DOCKER que se le asigno al servidor API.