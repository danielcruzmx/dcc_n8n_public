## Python y automatizaciones N8N con contenedores

- [Herramientas](#herramientas)
- [Instalación](#instalación)
- [Arranque y administración de contenedores](#arranque-y-administración-de-contenedores)
- [Conexión a base de datos PostgreSql](#conexión-a-base-de-datos-postgresql)
- [Creación de objetos](#creación-de-objetos)
- [Modelo de datos Northwind](#modelo-de-datos-northwind)
- [Documentación de la API REST de Python](#documentación-de-la-api-rest-de-python)  
- [Cache con Redis](#cache-con-redis) 
- [Inicio de N8N y licencia](#inicio-de-n8n-y-licencia)
- [Determinismo e IA](#determinismo-e-ia)
- [Inicio y configuración de Qdrant](#inicio-y-configuración-de-qdrant)
- [Bases de datos vectoriales e IA](#bases-de-datos-vectoriales-e-IA)
- [RAG Generación aumentada por recuperación](#rag-generación-aumentada-por-recuperación)
- [Descripción de plantillas](#descripción-de-plantillas)
- [Configuración para VPS](#configuración-para-vps)

### HERRAMIENTAS

Uso tres herramientas principales:

1. **Docker** que facilita la infraestructura
2. **Python** con sus frameworks ***FastApi*** para una rapida recuperación y actualización de datos y ***Flask*** para la ejecución de procesos en un servidor Web
3. **N8N** para la automatización e integracion con otras herramientas como agentes de IA, correo electronico, almacenamiento en la nube y mensajeria

Y como herramientas adicionales:

- **PostgreSql** -	Base de datos relacional
- **PGAdmin** -		Administrador de base de datos para PostgreSql
- **Redis** -		Cache
- **Qdrant** -		Base de datos vectorial para agentes de IA

### INSTALACIÓN

Como requisito indispensble se requiere tener instalado **DOCKER** o **PODMAN** y ***DOCKER COMPOSE***.

#### Archivo docker-compose.yml

- Tiene la configuración necesaria para arrancar los servicios en un **EQUIPO LOCAL**.
- Con algunos cambios puede llevarse a un ***VPS*** y trabajar con el protocolo ***HTTPS*** -ver configuración para VPS-.
- Define el volumen ***postgres-vol*** para persistir la base de datos.
- Define la red virtual ***vpn8n*** con el rango de direcciones 10.13.0.0/16
- Cada contenedor tiene asignada una dirección IP dentro del rango anterior.
- El volumen y la red virtual se crean automaticamente al arrancar un servicio con docker-compose
- En algunos servicios esta definido el usuario de acceso y su contraseña.

#### Imagenes de los contenedores

Descarga:

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

En la dirección ***http://localhost:8015*** esta PgAdmin, el administrador de la base de datos. Para acceder se requiere el correo y contraseña definidos en el archivo ***docker-compose.yml***.

En el administrador configure la conexión para PostgreSql, use el icono ***Agregar un Nuevo Servidor***, el nombre de la conexión puede ser por ejemplo ***local***. 

Ubique la ceja ***Conexión*** y especifique la ***Dirección del servidor***, debe ser la IP asignada al contenedor de PostgreSql ***10.13.0.2***, el usuario por default es ***postgres*** al igual que la base de datos. La contraseña esta definida en el archivo ***docker-compose.yml***

A la izquierda del administrador siempre vera el ***arbol de objetos*** de la base de datos, clic del boton derecho del raton sobre un objeto permite administrar sus elementos.

### CREACIÓN DE OBJETOS

Ubique el objeto ***Secuencias*** dentro de ***Esquemas*** y con la ayuda del boton derecho del raton cree la sequencia ***sq_ispt***, esta secuencia se va a requerir al momento de crear las tablas que sirven para realizar los ejemplos de automatización de este repositorio.

Abra con un editor el archivo ***crear_tablas.sql***, seleccione y copie al portapapeles su contenido.

En la parte superior de PgAdmin esta el menu ***Herramientas***, tome la opción ***Herramienta de Consulta***, en el área de edición pegue y ejecute (F5) el contenido de ***crear_tablas.sql***

Los objetos creados aparecen en el arbol de la izquierda dentro de ***Esquemas/Tablas***.

Los archivos ***tipo_tabla.csv*** y ***tabla_ispt.csv*** tienen los datos necesarios para poblar las tablas. 

Clic del boton derecho del raton sobre el nombre de cada tabla nos da la opcion de **Import/Export Data**. 

Seleccione ***Importar*** y a la derecha de ***Nombre de archivo*** de clic sobre el icono que sirve para administrar el directorio, ubique el menu de tres puntos ***...***, tome la opcion ***Upload*** que abre la ventana donde podra arrastrar los archivos de datos **.csv** y completar la tarea de importación.

### MODELO DE DATOS NORTHWIND

En el directorio ***database*** se encuentra la imagen ***.png*** y el script ***.sql*** del modelo de datos ***northwind***, instale con la ayuda del arbol de objetos.

 Botón derecho sobre el objeto ***Bases de Datos*** le permite creer la base de datos ***northwind***.

 Posteriormente abra una ***Herramienta de Consulta***, pegue y ejecute el script de creación de las tablas. El script tambien inserta datos para que de inmediato pueda ejecutar sentencias SQL.

No sabes SQL? 

https://dancruzmx.medium.com/aprende-sql-1ra-parte-conceptos-de-base-de-datos-63019da3124f

### DOCUMENTACIÓN DE LA API REST DE PYTHON

En la dirección ***http://localhost:4557/docs*** se muestra la documentación de los servicios API REST programados, clic del raton sobre una ruta especifica despliega mayor información.

- Parametros requeridos por el servicio, nombre y tipo.
- Botones para la ejecución del servicio ***Try it out*** y posteriormente ***Execute***.
- Area de respuesta, codigo, tipo de respuesta y resultado.
- Sentencia ***CURL*** de llamado.

Es importante estar atento a la caja de texto ***CURL***, esas lineas se usan para configurar nodos ***HTTP Request*** en N8N.

#### Creación de nuevos servicios

El codigo de esta API -de momento- esta hecho para tareas de consulta de datos. 

Es muy facil incorporar nuevas rutas -nuevos servicios- relacionados con los datos de nuevas tablas de la base de datos.

Simplemente hay que seguir los pasos:

1. Define la consulta SQL de recuperación de los datos en el archivo ***Catalogos/consultas.py***.
2. Define el BaseModel (esquema) de la respuesta SQL en el archivo ***Catalogos/esquemas.py***
3. Importa los objetos en el archivo ***Routers/catalogos.py*** y agrega el codigo para la nueva ruta tomando como base una ruta ya definida y en funcionamiento.

### CACHE CON REDIS

Cuando se llama a un servicio API REST por primera vez, se ejecuta la sentencia SQL para recuperar los datos y se almacenan en la instancia de ***REDIS*** con una llave de acceso. Para llamados posteriores la API recupera los datos de la instancia de ***REDIS***.

Es importante señalar que la definicion de la llave de acceso en ***REDIS*** tiene tiempo de vencimiento, esto significa que en algun momento la recuperación de los datos se hará nuevamente de la base de datos.

En teoria la recuperación de datos debe ser mas rapida del cache ***REDIS***. 

Se recomienda usar este mecanismo en tablas que no cambian sus datos constantemente, los catálogos por ejemplo.

### INICIO DE N8N Y LICENCIA

El servidor ***N8N*** esta en la dirección ***http://localhost:5678***

Cuando se entra por primera vez, aperece un formulario donde se solicita una direccion de correo valida y algunos datos adicionales incluida una contraseña. En esa dirección de correo llegará la llave para la licencia de N8N.

#### Activación de la licencia

En el ambiente de trabajo de ***N8N***, abajo a la izquierda, donde aparece el ***nombre del usuario*** está el menu de tres puntos ***...***, tome la opción ***Settings*** y posteriormente presione el botón ***Enter activation key***, digite la licencia que llego a su correo y acepte para completar el proceso de configuración.

#### Sobre N8N

Crear ***Workflows*** es muy sencillo, existen muchos video tutoriales en la red que puedes consultar.

Algunas de mis plantillas -***Workflows***- son muy sencillas, las de nodo unico sirven para ilustrar como debe configurarse y usarse un nodo dentro de una red de contenedores.

Otros ***Workflow*** son mas elaboradas y representan soluciones a problemas reales.

Lo que más me entusiasma de ***N8N*** no son los ***agentes de IA***, es su facilidad de integración con WhatsApp, Telegram, PostgreSql y la Suite de Google (Gmail, Drive, Hojas de cálculo, Documentos, Calendario, Contactos ...)

Mis soluciones se basan en scripts de Python y no soy hábil para desarrollar interfaces -***FrontEnd***-, entonces ***N8N*** me facilita esa tarea.

Recibo mensajes o correos con datos adjuntos que desencadenan la ejecución de una solución y dan la respuesta, ***por supuesto en modo desatendido***.

Inclusive ***N8N*** me brinda la posibilidad de generar formularios ***dinámicos*** para el ingreso de datos. El nodo ***Form*** tiene la opción de definir sus elementos con código ***JSON***, esto hace posible la construcción de formularios basados en datos previos.

### DETERMINISMO E IA

El determinismo en computación se refiere a que, dadas unas mismas entradas y condiciones iniciales, un algoritmo o sistema siempre producirá la misma salida y seguirá la misma secuencia de estados durante su ejecución. Es decir, su comportamiento es completamente predecible.

Muchas soluciones de IA son no deterministas, esto significa que ante la misma entrada pueden producir respuestas ligeramente diferentes en distintas ejecuciones. Aunque su naturaleza es probabilistica algunas aplicaciones de IA pueden ser deterministas, especialmente cuando:

- Se usan algoritmos clásicos (reglas lógicas).
- Se combinan modelos de IA con sistemas deterministas (recuperación de datos exactos, generación de consultas SQL o llamado a servicios API REST).

***N8N*** es una herramienta determinista por naturaleza (mismas entradas -> mismas salidas), entonces en ***N8N*** debes delegar a los agentes de IA tareas que requieran razonamiento, comprensión del lenguaje o toma de decisiones. 

Las tareas más adecuadas para IA incluyen:

- Procesamiento de lenguaje natural
- Generación de contenido
- Clasificación de datos
- **Extracción** de datos en documentos no estructurados
- Descomposición de tareas complejas
- Busqueda y sintesis de información

Toma esto en cuenta durante el aprendizaje de esta magnifica herramienta.

### INICIO Y CONFIGURACIÓN DE QDRANT

El panel de control de ***Qdrant*** esta en la dirección ***http://localhost:6333/dashboard***

Para usar la base de datos vectorial desde ***N8N*** hay que proteger la instancia con una llave de acceso (***API KEY***). 

El comando de sistema operativo ***ssh-keygen*** nos ayuda a generar dicha clave, es necesario conservarla en un lugar seguro porque va a ser requerida para configurar las credenciales de acceso a la base de datos.

En la parte superior derecha del panel de control de ***Qdrant*** se encuentra la opcion (icono llave) que permite establecer la llave de acceso generada previamente.

Las credenciales de conexión para los nodos ***Qdrant Vector Store*** requieren dos parámetros:

- La llave de acceso ***API KEY***
- La URL del servidor en la RED VIRTUAL DE DOCKER http://10.13.0.6:6333

### BASES DE DATOS VECTORIALES E IA

Los agentes de IA pueden usar bases de datos relacionales y NoSQL, pero las bases de datos vectoriales les resultan mas eficientes para tareas que requieren comprensión semántica, como búsquedas por similitud o recuperación de contexto.

Para los agentes de IA, las bases de datos vectoriales son esenciales para implementar marcos de recuperación aumentada (***RAG***), donde la consulta del usuario se convierte en un vector y se compara con otros vectores almacenados para encontrar documentos o información semánticamente similar. 

Lo anterior permite a los agentes proporcionar respuestas precisas y verificables, basadas en fuentes externas, evitando así las alucinaciones propias de los modelos de lenguaje grandes (***LLMs***), que pueden generar información falsa o irrelevante.

### RAG GENERACIÓN AUMENTADA POR RECUPERACIÓN

Es una técnica de IA que recupera información de fuentes externas y la utiliza como contexto para generar respuestas. Es útil en situaciones donde la actualidad y el contexto son cruciales para generar respuestas precisas y relevantes.

Funcionamiento:

1. ***Acopio de datos***, documentos o bases de datoa.
2. ***Segmentación de datos***, los datos se dividen en segmentos mas pequeños pra facilitar su administración y procesamiento.
3. ***Incrustación de documentos***, los fragmentos se transforman en incrustaciones o representaciones vectoriales. Son valores númericos que representan un valor semantico del contenido.
4. ***Gestión de consultas***, las consultas se convierten en representaciones vectoriales utilizando el mismo modelo de incrustación.
5. ***Recuperacion de la información***, el sistema compara la incrustación de la consulta con las incrustaciones de los documentos para identificar y recuperar los fragmentos de datos mas relevantes.
6. ***Generación de respuestas***, los fragmentos de texto seleccionados y la consulta original se introducen en un LLM que genera una respuesta coherente y contextualizada.
7. ***Actualización constante***, para mantener la relevancia y presición, los datos externos se deben acualizar constantemente.

Donde usar RAG:

- ***Asistencia al cliente y chatbots***, las respuestas proporcionadas se realizan en base a manuales de usuario y base de datos de productos.
- ***Analisis de riesgos financieros***, la información actualizada sobre tendencias del mercado e identificación de posibles riegos son la clave para una gestión finaciera efectiva.
- ***Asistentes de aprendizaje personalizado***, requiere de información del contenido educativo asi como las necesidades y ritmo de aprendizaje de cada estudiante. 

Retos:

- ***Integración de sistemas***, debe combinarse con un Modelo de Lenguaje (LLM).
- ***Escalabilidad y rendimiento***, La generación de incrustaciones y recuperación de datos en tiempo real son operaciones intensivas en computación.
- ***Calidad y actualización de los datos***, requiere la actualización constante de los documentos para mantener la pecisión del sistema.

### DESCRIPCIÓN DE PLANTILLAS

#### NOTA IMPORTANTE

**La comunicación entre los contenedores/servidores se da a través de las direcciones IP asignadas en la RED VIRTUAL DE DOCKER**. 

Cuando usamos el navegador para acceder a los servidores la dirección es ***localhost*** debido a que ***Docker*** establece un puente entre sus redes virtuales y la maquina huesped, el puerto es lo que hace la diferencia entre las aplicaciones.

#### - consulta_sql_postgres.json

Workflow de unico nodo del tipo ***Postgres execute SQL query***, ejecuta una consulta SQL a la base de datos Postrgres. 

La configuración de la conexión debe considerar que la dirección IP del host de base de datos es ***10.13.0.2***

#### - api_http_request.json

Workflow de unico nodo del tipo ***HTTP Request***, hace un llamado a la API de Python para recuperar información, la dirección del servicio debe ser ***http://10.13.0.5:4557/tablaispt*** 

Para conocer los servicios que brinda la API es necesario ver su documentación en la dirección ***http://localhost:4557/docs***. 

Cada servicio/ruta muestra el código de llamado via ***CURL***, ese código puede emplearse para configurar nodos ***HTTP Request*** (boton ***Import cURL***), solo hay que cambiar la dirección ***localhost*** por la IP de la RED VIRTUAL DE DOCKER que se le asigno al servidor API.

#### - dropdown_dinamico.json

El nodo ***Form*** de ***N8N*** permite definir con codigo JSON sus elementos, en este Workflow se usa esa modalidad.

```
[
   {
    "fieldLabel": "Equipo",
    "fieldType": "dropdown",
    "fieldOptions": {
      "values": {{ $json.values[0] }}
    },
    "requiredField": true
  }
]   
```

Los valores del combo desplegable ***dropdown*** se definen con la variable ***$json.values[0]*** no son ***valores fijos***. Esto permite condicionar los valores del combo en nodos previos.

#### - GeneraCaendarioNFL.json

Este Workflow surge de la necesidad de tener en mi Calendario de Google todos los juegos de la temporada regular de la NFL. 

Calendar de Google tiene la opcion de explorar y agregar calendarios ya establecidos, existen los calendarios de cada equipo y pueden agregarse con la ayuda de las opciones nativas de Calendar, pero se tiene el inconveniente de duplicidad de eventos, además siguen siendo eventos de otros calendarios, no de mi calendario.

La solución consiste en:

1. Identificar los ID de los calendarios de los equipos
2. Elaborar una lista en Google Sheet con los nombres de los equipos y los ID de sus calendarios
3. Crear un nodo ***Google Sheet*** que lea los registros de la lista
4. Crear un nodo ***Set*** para establecer las fechas de inicio y fin de la temporada
5. Crear un nodo ***Calendar*** que recupere los eventos de los equipos en las fechas determinadas
6. Crear un nodo ***Remove Duplicates*** para eliminar eventos duplicados
7. Crear un nodo ***Set*** que asigne a cada evento un ID propio
7. Crear un nodo ***Calendar*** que genere mis eventos (partidos) con los datos previos

Una vez generado mi propio calendario de juegos, la intención es construir otro Workflow que generare cada semana la lista de encuentros y la envie a mis contactos para que hagan sus pronósticos.

#### - carga_leyes.json 

Este Workflow es el ejemplo del uso de RAG, la descripción del flujo es:

1. Mediante formulario se ingresa un archivo PDF con la ley de propiedad en condominio de mi ciudad. 
2. Un agente de IA extrae la siguiente información del documento: 
	- Resumen 
	- Descripcion
	- Analisis
	- Conclusión  
	- Palabras clave
3. Al mismo tiempo un nodo con codigo JavaScript separa las leyes por TITULO, CAPITULO y ARTICULO.
4. Se combina la información de los puntos 2 y 3 (nodo Merge) 
5. Con la ayuda de un agente de IA se almacena la información en una base de datos vectorial.

***Estas acciones estan definidas en el funcionamiento de RAG***. La información recolectada debe ser segmentada y convertida a representaciones vectoriales.

Posterior a la carga de la ley condominal se hace lo mismo con el reglamento de la ley, la información de ambos documentos queda en la misma base de datos pero en colecciones distintas. 

#### - chat_condominios.json

Este Workflow es un chatbot "especializado" que responde preguntas relacionadas con la ley de propiedad en condominio de mi ciudad y su reglamento.

Usa la información almacenada con el Workflow ***carga-leyes.json***

#### - borra_coleccion.JSON

Este Workflow de unico nodo sirve para borrar colecciones de la base de datos vectorial. 

Si por alguna razón la ley de propiedad en condominio cambia hay que borrar su contenido de la base de datos y volverlo a cargar (Punto 7 del funcionamiento de un sistema RAG).   

No hay que olvidar que la referencia a la base de datos vectorial es:

http://10.13.0.6:6333

### CONFIGURACIÓN PARA VPS

Mi ***VPS*** esta en Hostinger, uso ***acme-companion*** que junto con ***nginx-proxy*** ayudan a automatizar completamente la obtención y renovación de certificados ***HTTPS*** de Let's Encrypt. 

https://github.com/nginx-proxy/acme-companion.git

Esta herramienta genera dos contenedores para su funcionamiento:

1. ***nginx-proxy*** que actúa como un proxy inverso que redirige el tráfico entrante (puertos 80 y 443) a los contenedores de aplicaciones según el dominio (RED VIRTUAL DE DOCKER). Se encarga de enrutar las solicitudes ***HTTP/HTTPS*** a los servicios correctos en la red Docker.

2. ***acme-companion*** que se encarga de obtener y renovar automáticamente certificados ***SSL/TLS*** de Let's Encrypt para los dominios configurados. Escucha los eventos de Docker y cuando detecta un contenedor con la variable ***LETSENCRYPT_HOST***, solicita un certificado mediante el protocolo ACME.

En resumen, el modelo es ideal para entornos Docker donde se desea HTTPS sencillo y automatizado.

En DigitalOcean uso una configuración similar, en su oportunidad lo documente

https://dancruzmx.medium.com/configuraci%C3%B3n-de-un-servidor-proxy-nginx-en-centos7-y-contenedores-docker-180b0440a6b7

#### Configuración para los contenedores

Con ***acme-companion*** solo se necesitan agrear las variables de ambiente ***VIRTUAL_HOST***, ***LETSENCRYPT_EMAIL*** y ***LETSENCRYPT_HOST***, como se muestra a continuación:

***Nota***.- En esta configuración la red virtual de docker se nombra ***podman*** y no se asignan direcciones IP a los contenedores, docker las asigna de manera automática, si requiere saber la IP asignada a un contenedor use la instrucción ***docker inspect Container_ID | grep IPAddress***

```
services:
    
    api:
        image: python3_fastapi1:latest
        volumes:
            - ./fastapi:/home
        environment:
            - VIRTUAL_HOST=api.midominio.com
            - LETSENCRYPT_HOST=api.midominio.com
            - LETSENCRYPT_EMAIL=api.main@gmail.com
            - HOSTDB=10.88.0.4
            - CACHE=10.88.0.26
            - USERDB=postgres
            - PASSDB=P0stgr3s
            - PORTDB=5432
            - DATABASE=postgres
        ports:
            - "0.0.0.0:4557:4557"
        entrypoint: /bin/bash -c 'cd /home && uvicorn main:app --host 0.0.0.0 --port 4557 --reload --workers 1 '
        tty: true
        networks: [default, proxy]

networks:
  proxy:
   external:
    name: podman
```

El servidor API REST queda en la dirección https://api.midominio.com/docs

Es importante mencionar que la herramienta ACME Companion requiere de un dominio válido para emitir certificados. Esto se debe a que el protocolo ACME valida la propiedad del dominio antes de emitir un certificado. ***Sin un dominio registrado y accesible, el proceso de verificación no puede completarse***. Debes poseer un dominio y tener control sobre su configuración DNS o servidor web.

No todos los contenedores deben ser configurados de esta manera, solo se deben configurar los servicios que deseas compartir o acceder en la nube. Por supuesto que el servidor de ***N8N*** debe ser uno de ellos.
