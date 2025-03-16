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
