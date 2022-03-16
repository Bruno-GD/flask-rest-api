# Flask REST API

## Instalación en local

1. Clonar el repositorio
2. ~~Establecer las variables de entorno~~ Revisar el archivo `.flaskenv`
```
FLASK_APP = "flaskr"
FLASK_ENV = "development" # o "production"
```
3. Instalar las librerías para mariadb
   * para Ubuntu:
   ```shell
   $ apt-get install gcc libmariadb3 libmariadb-dev
   ```
4. Instalar las dependencias
```shell
$ python -m pip install -r requirements.txt
```
5. Ejecutar el servidor flask
   * _previamente se necesita una base de datos MariaDB_
   * _configurar el archivo `.env` en `./flaskr/.env`_
```shell
$ flask run
```

## Instalación con Docker(-compose)

1. Clonar el repositorio
2. Ejecutar el docker-compose.yml
```shell
$ docker compose up 
```
_Esto creará dos contenedores, uno para MariaDB (MySQL Server) y otro para Flask_
