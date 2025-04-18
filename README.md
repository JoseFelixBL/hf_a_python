# Siguiendo los ejercicios de Head First Python

Estoy siguiendo los ejercicios del libro Head First Python para luego contenerizarlo y ejecutarlo en otro PC. 

De momento estoy con la app vsearch4web.py: buscar caracteres en un string, usando Flask.

## Contratiempos
Empecé en Windows 10, VSCode, pero no me funciona el uso de volúmenes BIND MOUNT: 
  - En Docker Desktop y en el activity bar de Docker se ven, pero no los tengo disponibles en mi contenedor, no aparecen.

### Solución
He probado desde VSCode en WSL/Ubuntu y ahí funciona perfectamente, así que me mudo a desarrollar en WSL.


# Log
## 2025/03/16 - Dockerizo vsearchweb.py
### Problema: No conecto localhost:5000 del host al contenedor
1. Solución desde Flask  
Agregar en `app.run(debug=True)`  

   `app.run(host='0.0.0.0', port=5000, debug=True)`  
También funciona sin el puerto ya que está expuesto en la línea del docker run  
  `app.run(host='0.0.0.0', debug=True)`  
  
    De momento esta es la solución que usaré.  

2. Solución desde docker
En 2 pasos:  
  2.1 En Docker Desktop/Settings/Resources/Network  
    - Enable host networking  
    - Apply & Restart  
    
    2.2 En docker run agregar  
    - `docker run --network host ...`  

## 2025/03/16 - Corregir imagen para poder usarla en RPi desde Windows

Con esta versión creo la imagen de producción en Windows y la puedo probar en Windows o pasarla a Rpi y probar en remoto.   

Creo un Dockerfile para producción donde quito lo de los volúmenes para hacer pruebas y dejo la copia directa de los directorios templates y static.  

Sigo la secuencia:  
- Crear imagen  
- Guardarla como .tar  
- Copiarla (rcp) a Rpi  
- En Rpi, cargar  del .tar a imagen  
- Crear el contenedor (docker run)  

### Problema:  
> WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested exec /usr/local/bin/python: exec format error
### Solución:  
Agregar en el dockerfile lo siguiente:  
```
ARG PLATFORM=linux/arm64/v8
FROM --platform=${PLATFORM} python:3.13.2-alpine3.21 
```

## 2025/03/21 - USER y bind_mount con usuario diferente -problemas de permisos

Al usar USER para no estar con root, al usar un bind_mount el directorio y los ficheros quedan con un usuario diferente y no permite modificarlos.  

Tampoco funciona si hago el bind_mount desde `docker run ...`.  

### By-pass
No crear ni usar usuario en Dockerfile.

## 2025/03/21 - `RUN --mount=type=bind,source=...` no hace nada

Al usar `RUN --mount=type=bind,source=...` en Dockerfile no se monta el directorio.  

### By-pass
Montar el  volumen desde `docker run --mount type=bind,...`  

- `docker run -it -p 5000:5000 --mount type=bind,source=/home/jose/workspace/docker/hf_a_python/var,dst=/usr/src/app/var 
vs_root:0.3`  

## 2025/04/18 - Versión arm64v8 en mariadb y update Docker en RPi 400
- Corregir vsearchweb.py
- Agregar la versión de mariadb para Raspberry Pi, `image: arm64v8/mariadb:latest`
- Desinstalar docker.io y docker-compose porque eran versiones desactualizadas (pasa en docker desde apt) y cargarlas directamente desde Docker con curl:  
  + `curl -sSL https://get-docker.com | sh`  
- subir a github
- descargarlo en RPi 400
- ejecutarlo  
  + `docker composae -f docker-compose.prod.ARM.yml up --build -d`  
  