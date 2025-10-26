## Descripción de la configuracion para VPS

Mi ***VPS*** esta en Hostinger, uso ***acme-companion*** que junto con ***nginx-proxy*** ayudan a automatizar completamente la obtención y renovación de certificados ***HTTPS*** de Let's Encrypt. 

https://github.com/nginx-proxy/acme-companion.git


El esquema con ***acme-companion*** genera dos contenedores principales para su funcionamiento:

1. ***nginx-proxy*** que actúa como un proxy inverso que redirige el tráfico entrante (puertos 80 y 443) a los contenedores de aplicaciones según el dominio (RED VIRTUAL DE DOCKER). Se encarga de enrutar las solicitudes ***HTTP/HTTPS*** a los servicios correctos en la red Docker.

2. ***acme-companion*** que se encarga de obtener y renovar automáticamente certificados ***SSL/TLS*** de Let's Encrypt para los dominios configurados. Escucha los eventos de Docker y cuando detecta un contenedor con la variable ***LETSENCRYPT_HOST***, solicita un certificado mediante el protocolo ACME.

En resumen, el modelo es ideal para entornos Docker donde se desea HTTPS sencillo y automatizado.

### CONFIGURACION PARA LOS CONTENEDORES

Solo se deben configurar con las variables de ambiente ***VIRTUAL_HOST*** y ***LETSENCRYPT_HOST*** los contenedores con los servicios que van a salir al exterior, por ejemplo: 

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

