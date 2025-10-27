## Python y automatizaciones N8N con contenedores

## INDICE
- [Herramientas](#herramientas)
- [Instalación](#instalación)
- [Arranque y dministración de contenedores](#arranque_y_administración-de-contenedores)
- [Conexión a base de datos PostgreSql](#conexión-a-base-de-datos-postgresql)
- [Modelo de datos Northwind](#modelo-de-datos-northwind)
- [Documentación de la API REST de Python](#documentación-de-la-api-rest-de-python)   

### HERRAMIENTAS

Uso tres herramientas principales:

1. **Docker** que facilita la infraestructura
2. **Python** con sus frameworks ***FastApi*** para una rapida recuperación y actualización de datos y ***Flask*** para la ejecución de procesos en un servidor web
3. **N8N** para la automatización e integracion con otras herramientas como agentes de IA, correo electronico, almacenamiento en la nube y mensajeria

Y como herramientas adicionales:

- **PostgreSql** -	Base de datos relacional
- **PGAdmin** -		Administrador de base de datos para PostgreSql
- **Redis** -		Cache
- **Qdrant** -		Base de datos vectorial para agentes de IA

### INSTALACIÓN

Como requisito indispensble se requiere tener instalado **DOCKER** o **PODMAN** y el complemento ***DOCKER COMPOSE***.

#### Archivo docker-compose.yml

- Tiene la configuración necesaria para arrancar los servicios en un **EQUIPO LOCAL**.
- Con algunos cambios puede llevarse a un ***VPS*** y trabajar con el protocolo ***HTTPS*** -ver directorio VPS_config-.
- Define el volumen ***postgres-vol*** para persistir la base de datos.
- Define la red virtual ***vpn8n*** con el rango de direcciones 10.13.0.0/16
- Cada contenedor tiene asignada una dirección IP dentro del rango anterior.
- El volumen y la red virtual se crean automaticamente al arrancar un servicio con docker-compose
- En algunos servicios esta definido el usuario de acceso y su contraseña.

#### Imagenes de los contenedores

Así se descargan:

```
docker pull postgres:latest
docker pull dpage/pgadmin4:latest 
docker pull redis:latest
docker pull qdrant/qdrant:latest
docker pull n8nio/n8n:latest
docker pull python:3.9-slim
```

Las imagenes para los servidores ***FastApi*** y ***Flask*** se construyen con la ayuda de los archivos ***dockerfile*** y ***requirements.txt*** ubicados en cada directorio.

Es necesario entrar al directorio correspondiente y ejecutar en cada directorio la instrucción:

```
docker build -t python3_flask2 -f dockerfile
docker build -t python3_fastapi1 -f dockerfile
```

### ARRANQUE Y ADMINISTRACIÓN DE CONTENEDORES

Recomiendo arrancar los servicios uno a uno en el siguiente orden:

```
docker-compose up -d db
docker-compose up -d admin_db
docker-compose up -d cache
docker-compose up -d api
docker-compose up -d qdrant
docker-compose up -d web
docker-compose up -d n8n
```

Para finalizar los servicios use:

```
docker-compose down
``` 

La instruccion anterior destruye los contenedores, mas adelante veremos como un contenedor puede pausar su ejecucion y reanudarla. 

Para conocer el estado de los contenedores use:

```
docker ps -a
```

La sentencia muestra la lista de los contenedores, identifique el ***Container_ID***, el ***Nombre*** y su ***Estado*** para que pueda hacer referencia a ellos.

En caso de problemas es necesario ver los ***logs*** del contenedor, use la instrucción:

```
docker logs Container_ID
```

Para ver los parámetros de configuracion del contenedor use:

```
docker inspect Container_ID
```

Un contenedor en estado ***UP*** puede ser pausado con:

```
docker stop Container_ID
```

Para reanudar la ejecucion de un contenedor use:

```
docker start Container_ID
```

Para destruir un contenedor use:

```
docker rm Container_ID
```

### CONEXIÓN A BASE DE DATOS POSTGRESQL

Para administrar la base de datos con PgAdmin entre a la dirección ***http://localhost:8015***, 
el correo y contraseña de acceso estan definidos en el archivo ***docker-compose.yml***.

En el administrador configure la conexión para PostgreSql, use el icono ***Agregar un Nuevo Servidor***, el nombre de la conexión puede ser por ejemplo ***local***. 

Ubique la ceja ***Conexión*** y especifique la ***Dirección del servidor***, debe ser la IP asignada al contenedor de PostgreSql ***10.13.0.2***, el usuario por default es ***postgres*** al igual que la base de datos, la contraseña esta definida en el ***docker-compose.yml***

A la izquierda del administrador siempre vera el ***arbol de objetos*** de la base de datos, clic del boton derecho del raton sobre un objeto permite administrar sus elementos.

### CREACIÓN DE OBJETOS

Ubique el objeto ***Secuencias*** dentro de ***Esquemas*** y con la ayuda del boton derecho del raton cree la sequencia ***sq_ispt***, esta secuencia se va a requerir al momento de crear las tablas que sirven para realizar los ejemplos de automatización de este repositorio.

Abra con un editor el archivo ***crear_tablas.sql***, seleccione y copie al portapapeles su contenido.

En la parte superior de PgAdmin esta el menu ***Herramientas***, tome la opción ***Herramienta de Consulta***, en el área de edición pegue y ejecute (F5) el contenido de ***crear_tablas.sql***

Los objetos creados aparecen en el arbol de la izquierda dentro de ***Esquemas/Tablas***.

Los archivos ***tipo_tabla.csv*** y ***tabla_ispt.csv*** tienen los datos necesarios para poblar las tablas. 

Clic del boton derecho del raton sobre el nombre de cada tabla nos da la opcion de **Import/Export Data**. 

Seleccione ***Importar*** y a la derecha de ***Nombre de archivo*** esta el icono que sirve para administrar el directorio, ubique el menu de tres puntos***...***, tiene la opcion ***Upload*** para abrir la ventana donde podra arrastrar los archivos de datos **.csv** y completar la tarea de importación.

### MODELO DE DATOS NORTHWIND

En este directorio se encuentra la imagen ***.png*** y el script ***.sql*** del modelo de datos ***northwind***, instale con la ayuda del arbol de objetos.

 Botón derecho sobre el objeto ***Bases de Datos*** le permite creer la base de datos ***northwind***.

 Posteriormente abra una ***Herramienta de Consulta***, pegue y ejecute el script de creación de las tablas. El script tambien inserta datos para que de inmediato pueda ejecutar sentencias SQL.

No sabes SQL? 

https://dancruzmx.medium.com/aprende-sql-1ra-parte-conceptos-de-base-de-datos-63019da3124f

### DOCUMENTACIÓN DE LA API REST DE PYTHON

En la dirección ***http://localhost:4557/docs*** se muestra la documentación de los servicios programados, clic del raton sobre una ruta especifica despliega mayor información.

- Parametros requeridos por el servicio, nombre y tipo
- Botones para la ejecución del servicio ***Try it out*** y posteriormente ***Execute***.
- Area de respuesta, codigo, tipo de respuesta y resultado.
- Sentencia ***curl*** de llamado

Es importante estar atento a la caja de texto ***curl***, esas lineas se usan para configurar nodos ***HTTP Request*** en N8N.

#### Creación de nuevos servicios

El codigo de esta API -de momento- esta hecho para tareas de consulta de datos. 

Es muy facil incorporar nuevas rutas -nuevos servicios- relacionados con los datos de nuevas tablas de la base de datos.

Simplemente hay que seguir los pasos:

1. Define la consulta SQL de recuperación de los datos en el archivo ***Catalogos/consultas.py***.
2. Define el BaseModel (esquema) de la respuesta SQL en el archivo ***Catalogos/esquemas.py***
3. Importa los objetos en el archivo ***Routers/catalogos.py*** y agrega el codigo para la nueva ruta tomando como base una ruta ya definida y en funcionamiento.




Ver README.md de cada directorio.

- ***/database***	-		Inicio del administrador de base de datos y creacion de tablas
- ***/fastapi*** 	-		Uso de la API REST de Python
- ***/flask*** 		- 		Arranque y uso del servidor Web
- ***/plantillas*** -		Descripcion de las plantillas n8n
- ***/qdrant*** 	-		Configuración del servicio
- ***/n8n_data*** 	-		Inicio de n8n y licencia
- ***/VPS_config*** -		Descripción de la configuracion para VPS

