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

## 2025/04/23 - Agregar mariadb_admin para hacer backups de los logs  

Como ejercicio he creado otro servicio en docker compose para llevar a cabo labores de mantenimiento sin tener que parar el servicio, específicamente, hacer un backup de la base de datos `vsearchlogDB`.  

No ha hecho falta modificar `docker-compose.prod.ARM.yml`, solo se ha agregado un directorio `database_admin` y dentro de él: `docker-compose.prod.yml` con la definición del contenedor y la acción a realizar.

Tener los docker-compose separados nos permite elegir si queremos:  
- Iniciar el servicio:
  - `docker compose -f docker-compose.prod.ARM.yml up -d`
- Hacer un Backup en un servicio iniciado:  
  - `docker compose -f docker-compose.prod.ARM.yml -f ./database_admin/docker-compose.prod.yml up db_admin`  
- Iniciar el servicio y hacer un backup de inmediato:
  - Esta opción mejor no intentarla porque la base de datos tarda en arrancar porque hace procesos de inicio, pero como el demonio está arrancado el servicio db_admin intenta conectar a la base de datos y no está disponible...  
  - `docker compose -f docker-compose.prod.ARM.yml -f ./database_admin/docker-compose.prod.yml up -d`  

He decidido crear el shell-script y montarlo en el volumen para ponerle nombres significativos a los ficheros generados agregando el nombre de la base de datos y la fecha y hore del backup.  

## 2025/04/23 - Error response from daemon: failed to setup copntainer networking: network ae3b... not found  

Al parecer este error puede aparecer cuando eliminamos redes con `docker network prune`, en algún lado se queda la referencia a una red anterior que trata de encontrar.

Para resolverlo, agregar la opción `--force-recreate` al final del `docker compose up --force-recreate`
