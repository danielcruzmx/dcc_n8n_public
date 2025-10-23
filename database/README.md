# CONFIGURACION DEL ADMINISTRADOR PGADMIN PARA POSTGRESQL 

## CREACION DE OBJETOS (TABLAS)

Despues de arrancar el contenedor de base de datos y el administrador PgAdmin puede entrar a el en la dirección *http://localhost:8015*, el correo y contraseña se definieron en el *docker-compose.yml* servicio *admin_db*.

Configure la conexión para PostgreSql usando el icono *"Add new Server"*, el nombre puede ser por ejemplo *"local"*. 

En la ceja de los parametros de conexión la *URL del servidor* debe ser la IP asignada al contenedor de PostgreSql (**10.13.0.2 según docker.compose.yml**), el usuario por default es *postgres* al igual que la base de datos, la contraseña esta definida en el *docker-compose.yml* servicio *db*.

A la izquierda del administrador siempre vera el arbol de objetos de la base de datos, clic del boton derecho del raton sobre un objeto permite crear elementos.

Sobre el objeto *Secuencias* cree la sequencia *sq_ispt*, esta secuencia se va a requerir al momento de crear las tablas que serviran para realizar algunos ejemplos de automatización que veremos posteriormente.

Para crear las tablas, en el **menu Herramientas** de PgAdmin tome la opción *herramienta de consulta*, copie y ejecute el contenido del script *crear_tablas.sql* ubicado en este directorio.

Los archivos *tipo_tabla.csv* y *tabla_ispt.csv* tienen los datos necesarios para poblar las tablas. Clic del boton derecho del raton sobre el nombre de la tabla nos da la opcion de Importar/Exportar datos. Seleccione *Importar* y a la derecha del nombre el archivo esta el icono que sirve para manejar el directorio, el menu de **...** da la opcion *Upload* que abre la ventana donde podra arrastrar los archivos de datos y completar la tarea de importación.








