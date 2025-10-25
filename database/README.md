## Inicio del administrador de base de datos y creacion de tablas

### CREACION DE OBJETOS (TABLAS)

Para administrar la base de datos con PgAdmin entre a la dirección ***http://localhost:8015*** 

El correo y contraseña de acceso estan definidos en el archivo ***docker-compose.yml***, en el apartado del servicio ***admin_db***.

Dentro del administrador configure la conexión para PostgreSql usando el icono ***Agregar un Nuevo Servidor***, el nombre de la conexión puede ser por ejemplo ***local***. 

Ubique la ceja ***Conexión*** y especifique la ***Dirección del servidor***, debe ser la IP asignada al contenedor de PostgreSql ***10.13.0.2 -ver archivo docker.compose.yml-***.

El usuario por default es ***postgres*** al igual que la base de datos, la contraseña esta definida en el archivo ***docker-compose.yml***, en el aprtado del servicio ***db***.

A la izquierda del administrador siempre vera el arbol de objetos de la base de datos, clic del boton derecho del raton sobre un objeto permite administrar los elementos.

Ubique el objeto ***Secuencias*** dentro de ***Esquemas*** y con la ayuda del boton derecho del raton cree la sequencia ***sq_ispt***, esta secuencia se va a requerir al momento de crear las tablas que sirven para realizar los ejemplos de automatización de este repositorio.

Para crear las tablas, ubique en la parte superior de PgAdmin el **menu Herramientas** y tome la opción ***Herramienta de consulta***, en el área de edición de las consultas copie y ejecute el contenido del script ***crear_tablas.sql***

Los objetos creados aparecen en el arbol de la izquierda dentro de ***Esquemas/Tablas***.

Los archivos ***tipo_tabla.csv*** y ***tabla_ispt.csv*** tienen los datos necesarios para poblar las tablas. 

Clic del boton derecho del raton sobre el nombre de cada tabla nos da la opcion de **Importar/Exportar** datos. 

Seleccione ***Importar*** y a la derecha del nombre el archivo esta el icono que sirve para manejar el directorio, el menu ***...*** tiene la opcion ***Upload*** que abre la ventana donde podra arrastrar los archivos de datos **.csv** y completar la tarea de importación.

## MODELO DE DATOS NORTHWIND

En este directorio se encuentra la imagen ***.png*** y el script ***.sql*** del modelo de datos ***northwind***, con la ayuda del arbol de objetos cree la base de datos ***northwind***, abra una ***Herramienta de consulta***, copie y ejecute el script de creación de las tablas, el script tambien inserta datos para que de inmediato puedas ejecutar sentencias SQL.

No sabes SQL? 

https://dancruzmx.medium.com/aprende-sql-1ra-parte-conceptos-de-base-de-datos-63019da3124f






