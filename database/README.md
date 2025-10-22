- CONFIGURACION DEL ADMINISTRADOR PGADMIN DE POSTGRESQL Y CREACION DE OBJETOS (TABLAS)

Despues de arrancar el administrador de PostgreSql puedes entrar a el en la dirección http://localhost:8015 el correo y contraseña se definieron en el docker-compose.yml

Configura la conexión hacia PostgreSql usando el icono "Add new Server", el nombre puede ser "local" por ejemplo, en los parametros de conexión la URL del servidor debe ser la IP asignada al contenedor de PostgreSql (10.13.0.2 según docker.compose.yml), el usuario por default es "postgres" al igual que la base de datos y la contraseña se definio en el docker-compose.yml

A la izquierda del administrador siempre se vera el arbol de objetos de la base de datos, clic del boton derecho del raton sobre un objeto permite crear elementos.

Sobre el objeto "Secuencias" cree la sequencia "sq_ispt", esta secuencia se va a requerir al momento de crear las tablas que serviran para realizar algunos ejemplos de automatización que veremos posteriormente.

Desde el menu Herramientas de PgAdmin abra una area de consulta (SQL), copie y ejecute el script "crear_tablas.sql" ubicado en este directorio.







