# Python y automatizaciones N8N con contenedores

## RESUMEN

En este repositorio uso 3 herramientas principales:

1. **Docker** que facilita la infraestructura
2. **Python** con sus frameworks ***FastApi*** para una rapida recuperación y actualización de datos y ***Flask*** para la ejecución de procesos en un servidor web
3. **N8N** para la automatización e integracion con otras herramientas como agentes de IA, correo electronico, almacenamiento en la nube y mensajeria

Como herramientas adicionales:

- **PostgreSql** -	Base de datos relacional
- **PGAdmin** -		Administrador de base de datos para PostgreSql
- **Redis** -		Cache
- **Qdrant** -		Base de datos vectorial para agentes de IA

## INSTALACION

Como requisito indispensble se requiere tener instalado **DOCKER** o **PODMAN** y el complemento ***DOCKER COMPOSE***.

El archivo ***docker-compose.yml*** tiene la configuración para arrancar los servicios en un **EQUIPO LOCAL**, con algunos cambios puede llevarse a un ***VPS*** para trabajar en la nube con el protocolo ***HTTPS*** -ver directorio VPS_config-.

Las imagenes base se descargan asi:

- **docker pull postgres:latest**
- **docker pull dpage/pgadmin4:latest** 
- **docker pull redis:latest**
- **docker pull qdrant/qdrant:latest**
- **docker pull n8nio/n8n:latest**
- **docker pull python:3.9-slim**

Las imagenes para los servidores ***FastApi*** y ***Flask*** se construyen con la ayuda de los archivos ***dockerfile*** y ***requirements.txt*** ubicados en cada directorio.

Es necesario entrar al directorio correspondiente y ejecutar en cada directorio la instrucción:

- ***docker build -t python3_flask2 -f dockerfile***
- ***docker build -t python3_fastapi1 -f dockerfile***

## ARRANQUE Y ADMINISTRACION DE LOS CONTENEDORES

Recomiendo arrancar los servicios uno a uno en el siguiente orden:

- ***docker-compose up -d db***
- ***docker-compose up -d admin_db***
- ***docker-compose up -d cache***
- ***docker-compose up -d api***
- ***docker-compose up -d qdrant***
- ***docker-compose up -d web***
- ***docker-compose up -d n8n***

Al final de cada instrucción va el nombre del servicio que se definido en el archivo ***docker-compose.yml***

Para finalizar los servicios use:

- ***docker-compose down*** 

La instruccion anterior destruye los contenedores, mas adelante veremos como un contenedor puede pausar su ejecucion y reanudarla. 

En el archivo ***docker-compose.yml*** se define el volumen ***postgres-vol*** y la red virtual ***vpn8n***, ambos se crean al momento de arrancar cualquiera de los servicios.

Para conocer el estado de los contenedores use:

- ***docker ps -a***

La sentencia muestra la lista de los contenedores, identifique el ***Container_ID***, el ***Nombre*** y su ***Estado*** para que pueda hacer referencia a ellos.

En caso de problemas es necesario ver los ***logs*** del contenedor, use la instrucción:

- ***docker logs Container_ID***

Para ver los parámetros de configuracion del contenedor use:

- ***docker inspect Container_ID***

Un contenedor en estado ***UP*** puede ser pausado con:

- ***docker stop Container_ID***

Para reanudar la ejecucion de un contenedor use:

- ***docker start Container_ID***

Para destruir un contenedor use:

- ***docker rm Container_ID***

## USO DE LOS SERVICIOS

Ver README.md en cada directorio del repositorio

- ***/database***	-		Inicio del administrador de base de datos y creacion de tablas
- ***/fastapi*** 	-		Uso de la api REST de Python
- ***/flask*** 		- 		Arranque y uso del servidor Web
- ***/plantillas*** -		Descripcion de las plantillas n8n
- ***/qdrant*** 	-		Conceptos sobre base de datos vectoriales y agentes de IA
- ***/n8n_data*** 	-		Inicio de n8n y licencia
- ***/VPS_config*** -		Descripción de la configuracion para VPS




