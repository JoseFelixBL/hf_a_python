# Instalar MariaDB
> sudo apt install mariadb-server

# Inicia el servidor

> sudo service mysql start

# Iniciar el aseguramiento del servidor

> sudo mysql_secure_installation

# Crear usuario con todos los permisos

> sudo mysql -u root

CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'contraseña';

GRANT ALL PRIVILEGES ON * . * TO 'usuario'@'localhost';

FLUSH PRIVILEGES;

EXIT;

# Activar Log de Consultas
> sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf

En la sección [server] (generalmente la primera) pega las siguientes lineas, guarda con Ctrl + O y sal del editor con Ctrl + X

general_log_file = /var/log/mysql/mysql.log
general_log = 1  

# Ejemplo de DB
## Crear DB, tablas, insertar datos
'''
CREATE DATABASE IF NOT EXISTS test;

USE test;

CREATE TABLE IF NOT EXISTS books (
  BookID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
  Title VARCHAR(100) NOT NULL, 
  SeriesID INT, AuthorID INT);

CREATE TABLE IF NOT EXISTS authors 
(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT);

CREATE TABLE IF NOT EXISTS series 
(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT);

INSERT INTO books (Title,SeriesID,AuthorID) 
VALUES('The Fellowship of the Ring',1,1), 
      ('The Two Towers',1,1), ('The Return of the King',1,1),  
      ('The Sum of All Men',2,2), ('Brotherhood of the Wolf',2,2), 
      ('Wizardborn',2,2), ('The Hobbbit',0,1);
'''  

## Algunos comandos
`SHOW TABLES;`  
`DESCRIBE Books;`  
`SELECT * FROM Books;`  
```
INSERT INTO books (Title, SeriesID, AuthorID)
VALUES ("Lair of Bones", 2, 2);
```  
```
UPDATE books 
SET Title = "The Hobbit" 
WHERE BookID = 7;
```
