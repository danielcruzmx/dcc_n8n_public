# Python y automatizaciones N8N con contenedores

## RESUMEN

Este repositorio usa 3 herramientas que ayudan a resolver problemas.

1. **Docker** que facilita la infraestructura.
2. **Python** con sus frameworks FastApi para una rapida recuperación y actualización de datos y Flask para la ejecución de diversos procesos.
3. **N8N** para la automatización e integracion con otras herramientas como agentes de IA, correo electronico, almacenamiento en la nube y mensajeria.

Como herramientas adicionales estan:

- **PostgreSql** -	Base de datos relacional.
- **PGAdmin** -		Administrador de base de datos PostgreSql.
- **Redis** -		Cache. 
- **Qdrant** -		Base de datos vectorial para agentes de IA.

## INSTALACION

Como requisito indispensble se requiere tener instalado **DOCKER** o **PODMAN**.

El archivo *docker-compose.yml* arranca los servicios en un EQUIPO LOCAL y con algunos cambios en su configuración pueden llevarse a un VPS y trabajar en la nube via HTTPS (directorio VPS_config).

Las imagenes base pueden descargarse asi:

- *docker pull postgres:latest*
- *docker pull dpage/pgadmin4:latest* 
- *docker pull redis:latest*
- *docker pull qdrant/qdrant:latest*
- *docker pull n8nio/n8n:latest*
- *docker pull python:3.9-slim*

Las imagenes de FastApi y Flask basadas en la imagen *python:3.9-slim* se construyen con la ayuda del archivo *dockerfile* y *requirements.txt* ubicados en cada directorio, es necesario entrar al directorio correspondiente y ejecutar en cada directorio la instrucción:

- *docker build -t python3_flask2 -f dockerfile*
- *docker build -t python3_fastapi1 -f dockerfile*

## ARRANQUE Y ADMINISTRACION DE LOS CONTENEDORES

Recomiendo arrancar los servicios uno a uno de la siguiente manera:

- *docker-compose up -d db*
- *docker-compose up -d admin_db*
- *docker-compose up -d cache*
- *docker-compose up -d api*
- *docker-compose up -d qdrant*
- *docker-compose up -d web*
- *docker-compose up -d n8n*

Al final va el nombre del servicio definido en el *docker-compose.yml*

Para finalizar los servicios use:

- *docker-compose down* 

La instruccion anterior destruye los contenedores, mas adelante veremos que un contenedor puede pausar su ejecucion o renudarla sin destruirlo. 

El volumen *postgres-vol* y la red *vpn8n* se crean al momento de arrancar cualquiera de los servicios.

Para conocer el estado de los contenedores use:

- *docker ps -a*

De la lista identifique el *Container_ID* o el *Nombre* para que pueda hacer referencia a un contenedor y en caso de problemas pueda ver los *logs* de la siguiente manera:

- *docker logs Container_ID*

Un contenedor en estado *UP* puede ser pausado con:

- *docker stop Container_ID*

Para reanudar la ejecucion de un contenedor:

- *docker start Container_ID*

Para destruir un contenedor use *"rm"* despues de pausar su ejecucion.

- *docker rm Container_ID*

## CONFIGURACION Y USO DE LOS CONTENEDORES

Ver README.md en cada directorio del repositorio

- **/database**	-		Uso del administrador de base de datos y creacion de tablas
- **/fastapi** -		Uso de la api
- **/flask** - 			Arranque y uso del servidor Web
- **/plantillas** -		Descripcion de las plantillas n8n
- **/qdrant** -			Conceptos sobre base de datos vectoriales y agentes de IA
- **/n8n_data** -		Configuración de n8n
- **/VPS_config** -		Descripcion de la configuracion para VPS




