# Pruebas de mariadb en Python  
Entrar en python para introducir los siguientes comandos:  

## Datos de configuración  
```
dbconfig = { 'host': '127.0.0.1', 
                 'user': 'vsearch', 
                 'password': 'vsearchpasswd', 
                 'database': 'vsearchlogDB', }
```  

## Importar librería
`import mariadb`  

## Conectar con el servcidor de BBDD - mariadb  
`conn = mariadb.connect(**dbconfig)`  

## Abrir un cursor  
`cursor = conn.cursor()`  

## Hacer consultas SQL  

```
_SQL = """show tables"""
cursor.execute(_SQL)
res = cursor.fetchall()
res

 _SQL = """describe log"""
cursor.execute(_SQL)
res = cursor.fetchall()
res

for row in res:
    print(row)
```  

## Insertar datos  
```
_SQL = """insert into log  
              (phrase, letters, ip, browser_string, results) 
              values 
              ('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""
cursor.execute(_SQL)
```  

### Una forma mejor:  
```
_SQL = """insert into log  
              (phrase, letters, ip, browser_string, results) 
              values 
              (%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()'))
```

### Hay que "comitear" los datos  
```
conn.commit() 
_SQL = """select * from log""" 
cursor.execute(_SQL) 
for row in cursor.fetchall(): 
    print(row) 
```  

### ...y cerrar al final  
```
cursor.close()
conn.close()
```