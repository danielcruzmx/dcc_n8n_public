## Descripción de la configuracion para VPS

### ACME

Mi ***VPS*** esta en Hostinger, uso ***acme-companion*** que junto con ***nginx-proxy*** ayudan a automatizar completamente la obtención y renovación de certificados ***HTTPS*** de Let's Encrypt. 

https://github.com/nginx-proxy/acme-companion.git

Esta herramienta genera dos contenedores para su funcionamiento:

1. ***nginx-proxy*** que actúa como un proxy inverso que redirige el tráfico entrante (puertos 80 y 443) a los contenedores de aplicaciones según el dominio (RED VIRTUAL DE DOCKER). Se encarga de enrutar las solicitudes ***HTTP/HTTPS*** a los servicios correctos en la red Docker.

2. ***acme-companion*** que se encarga de obtener y renovar automáticamente certificados ***SSL/TLS*** de Let's Encrypt para los dominios configurados. Escucha los eventos de Docker y cuando detecta un contenedor con la variable ***LETSENCRYPT_HOST***, solicita un certificado mediante el protocolo ACME.

En resumen, el modelo es ideal para entornos Docker donde se desea HTTPS sencillo y automatizado.

En DigitalOcean tengo esta configuración y en su oportunidad lo documente

https://dancruzmx.medium.com/configuraci%C3%B3n-de-un-servidor-proxy-nginx-en-centos7-y-contenedores-docker-180b0440a6b7

### CONFIGURACION PARA LOS CONTENEDORES

Con ***acme-companion*** solo se necesitan agrear las variables de ambiente ***VIRTUAL_HOST***, ***LETSENCRYPT_EMAIL*** y ***LETSENCRYPT_HOST***, como se muestra a continuación:

***Nota***.- En esta configuración la red virtual de docker se nombra ***podman*** y no se asignan direcciones IP a los contenedores, docker las asigna de manera automática, si requiere saber la IP asignada use la instrucción ***docker inspect Container_ID | grep IPAddress***

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

El servidor API REST esta en la dirección https://api.midominio.com/docs

Es importante mencionar que la herramienta ACME Companion requiere de un dominio válido para emitir certificados. Esto se debe a que el protocolo ACME valida la propiedad del dominio antes de emitir un certificado. ***Sin un dominio registrado y accesible, el proceso de verificación no puede completarse***. Debes poseer un dominio y tener control sobre su configuración DNS o servidor web.

No todos los contenedores deben ser configurados de esta manera, solo se deben configurar los servicios que deseas compartir o acceder en la nube. Por supuesto que el servidor de ***N8N*** debe ser uno de ellos.





