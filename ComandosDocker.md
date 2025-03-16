# Comandos Docker para recordar

## Imágenes
- Crear imagen  
    `docker build -t <nombre> .`  
    + Ejemplo:  
      `docker build -t vsweb:1.12 .`

- Ver imágenes creadas disponibles  
    `docker images`

- Borrar imágenes  
    `docker image rm <id>`  

- Guardar imagen en .tar  
    `docker image save -o <output.tar file> <image name>`  
    `docker image save -o vsw_prod1.0.tar vsweb_prod:1.0`  

- Recuperar imágenes de un .tar  
    `docker image load -i <fichero .tar>`

## Contenedores
- Crear un contenedor  
    `docker run <imagen>`  
    + Ejemplo:  
        `docker run -it -p 5000:5000 -v ./static:/usr/src/app/static -v ./templates:/usr/src/app/templates vsweb:1.12 sh`

- Ver contenedores corriendo:  
    `docker ps`  
    + Ver los que están corriendo y los parados:  
        `docker ps -a`

- Ejecutar un comando en un contenedor:  
    `docker exec <ID> <cmd>`  
    + Ejemplo:  
        `docker exec -it 123456789 sh`

- Borrar contenedores parados  
    `docker container prune`  
    + También: docker container rm <id>
