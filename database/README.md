## Inicio del administrador de base de datos y creacion de tablas

### ADMINISTRACION DE OBJETOS

Para administrar la base de datos con PgAdmin entre a la dirección ***http://localhost:8015***, 
el correo y contraseña de acceso estan definidos en el archivo ***docker-compose.yml***.

En el administrador configure la conexión para PostgreSql, use el icono ***Agregar un Nuevo Servidor***, el nombre de la conexión puede ser por ejemplo ***local***. 

Ubique la ceja ***Conexión*** y especifique la ***Dirección del servidor***, debe ser la IP asignada al contenedor de PostgreSql ***10.13.0.2***, el usuario por default es ***postgres*** al igual que la base de datos, la contraseña esta definida en el ***docker-compose.yml***

A la izquierda del administrador siempre vera el ***arbol de objetos*** de la base de datos, clic del boton derecho del raton sobre un objeto permite administrar sus elementos.

Ubique el objeto ***Secuencias*** dentro de ***Esquemas*** y con la ayuda del boton derecho del raton cree la sequencia ***sq_ispt***, esta secuencia se va a requerir al momento de crear las tablas que sirven para realizar los ejemplos de automatización de este repositorio.

#### Creación de tablas 

Abra con un editor el archivo ***crear_tablas.sql***, seleccione y copie al portapapeles su contenido.

En la parte superior de PgAdmin esta el menu ***Herramientas***, tome la opción ***Herramienta de Consulta***, en el área de edición pegue y ejecute (F5) el contenido de ***crear_tablas.sql***

Los objetos creados aparecen en el arbol de la izquierda dentro de ***Esquemas/Tablas***.

Los archivos ***tipo_tabla.csv*** y ***tabla_ispt.csv*** tienen los datos necesarios para poblar las tablas. 

Clic del boton derecho del raton sobre el nombre de cada tabla nos da la opcion de **Import/Export Data**. 

Seleccione ***Importar*** y a la derecha de ***Nombre de archivo*** esta el icono que sirve para administrar el directorio, ubique el menu ***...***, tiene la opcion ***Upload*** que abre la ventana donde podra arrastrar los archivos de datos **.csv** y completar la tarea de importación.

#### Modelo de datos Northwind

En este directorio se encuentra la imagen ***.png*** y el script ***.sql*** del modelo de datos ***northwind***, instale con la ayuda del arbol de objetos.

 Botón derecho sobre el objeto ***Bases de Datos*** le permite creer la base de datos ***northwind***.

 Posteriormente abra una ***Herramienta de Consulta***, pegue y ejecute el script de creación de las tablas, el script tambien inserta datos para que de inmediato pueda ejecutar sentencias SQL.

No sabes SQL? 

https://dancruzmx.medium.com/aprende-sql-1ra-parte-conceptos-de-base-de-datos-63019da3124f






