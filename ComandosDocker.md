# Comandos Docker para recordar

## Imágenes
- Crear imagen  
    `docker build -t <nombre> .`  
    + Ejemplo:  
      `docker build -t vsweb:1.12 .`  
- Crear imagen usando Dockerfile con otro nombre  
    `docker build -t <nombre> -f <Docker file name> .`  
    + Ejemplo:  
      `docker build -t vsweb:1.12 --file DockerfileProd .`  


- Ver imágenes creadas disponibles  
    `docker images`  
    + También se puede usar:  
    `docker image ls`  
    + `-q` para ver solo los IDs:  
    `docker image ls -q`  

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

- Ver contenedores:  
    + activos:  
    `docker container ls`  
    + todos, me da el status:  
    `docker container ls -a`  
    + ver solo los IDs:  
    `docker container ls -aq`  
    + ejemplo para borrar todos los contenedores, el `rm -f` es para borrar contenedores aunque estén corriendo:  
    `docker container rm -f $(docker container ls -aq)`  


- Ejecutar un comando en un contenedor:  
    `docker exec <ID> <cmd>`  
    + Ejemplo:  
        `docker exec -it 123456789 sh`

- Borrar contenedores parados  
    `docker container prune`  
    + También:  
    `docker container rm <id>`  


# JSON vs. YAML
## JSON: Para transferir datos entre sistemas  

Ejemplo:  
```
  nombre: José
  apellido: Bello
  edad: 25
  activo: true
  etiquetas:
    - Instructor 
    - Desarrollador
  direccion: 
    calle: Pepito
    numero: 51
```  
## YAML - o YML - Para archivos de configuración  

Ejemplo:  
```
{
  nombre: José,
  apellido: Bello,
  edad: 25,
  activo: true,
  etiquetas: [Instructor, Desarrollador],
  direccion: {
    calle: Pepito,
    numero: 51
  }
}
```  

# Trabajando con múltiples contenedores - docker-compose.yml  

## Partes de docker-compose.yml

### Servicios o imágenes
Las imágenes con las que vamos a trabajar se definen como `services:` y dentro se le da un nombre indentado a cada servicio:  
  ```
  services:
    app:
    api:
    db:
  ```  

De esta forma los servicios se podrán comunicar entre ellos por el nombre del servicio en vez de usar las IPs.  

#### Imágen dentro de nuestro servicio
##### Imagen de Dockerfile que hemos creado
La definimos con `build: <ruta del Dockerfile>`

##### Imagen bajada de Dockerhub
Si para uno de nuestros servicios no tenemos código y lo que hacemos es bajarnos una imagen usando `image:`  

#### Exponer puertos de nuestro servicio
Para exponer puertos usamos `port:` y en la línea siguiente, indentado, `- <host port>:<container port>`  

#### Volumen dentro de nuestro servicio
`volumes:`, siguiente línea indentado `- <source>:<target>` donde `<source>` puede ser nombre del volumen definido en el general, o si quiero _bind-mount_, la ruta dentro de mi host, p.e.: `.` o `./src`  

#### Variables de entorno
Se definen con `environment:` y siguiente línea indentado `<nombre variable de entorno>: <ruta>`

### Volúmenes
Para definir volúmenes, al mismo nivel de `services:` ponemos `volumes:`, siguiente línea `  <nombre del volumen>:`  

Ejemplo:  
```
service:
  app:
    build: ./frontend
    ports:
      - 80:5173
    volumes:
      - ./frontend/src:/app/src
  api:
    build: ./backend
    ports:
      - 3000:3000
    environment:
      DB_URL: mongodb://db/gamify
    volumes:
      - ./backend/app:/app/app
  db:
    image: mongo:5.0.19-focal
    port:
      - 27017:27017
    volumes:
      - gamify:/data/db

volumes:
  gamify:
```  
## Ejecutar docker compose
`docker compose up` para ejecutar todo lo que necesitamos/hemos edfinido en el _docker-compose.yml_.  
