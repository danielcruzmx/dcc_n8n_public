## Python y automatizaciones N8N con contenedores

## INDICE
- [Herramientas](#herramientas)
- [Instalación](#instalación)
- [Administración de contenedores](#administracion-de-contenedores)
- [Uso](#uso)
- [Documentación](#documentación)
- [Estructura del Proyecto](#estructura-del-proyecto)   

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

#### docker-compose.yml

- Tiene la configuración necesaria para arrancar los servicios en un **EQUIPO LOCAL**.
- Con algunos cambios puede llevarse a un ***VPS*** y trabajar con el protocolo ***HTTPS*** -ver directorio VPS_config-.
- Define el volumen ***postgres-vol*** para persistir la base de datos.
- Define la red virtual ***vpn8n*** con el rango de direcciones 10.13.0.0/16
- Cada contenedor tiene asignada una dirección IP dentro del rango anterior.
- El volumen y la red virtual se crean automaticamente al arrancar un servicio con docker-compose
- En algunos servicios esta definido el usuario de acceso y su contraseña.

#### Imagenes

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

#### Arranque

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

### USO DE LOS SERVICIOS

Ver README.md de cada directorio.

- ***/database***	-		Inicio del administrador de base de datos y creacion de tablas
- ***/fastapi*** 	-		Uso de la API REST de Python
- ***/flask*** 		- 		Arranque y uso del servidor Web
- ***/plantillas*** -		Descripcion de las plantillas n8n
- ***/qdrant*** 	-		Configuración del servicio
- ***/n8n_data*** 	-		Inicio de n8n y licencia
- ***/VPS_config*** -		Descripción de la configuracion para VPS

