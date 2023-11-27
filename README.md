# README:

## Manual de configuración

1. Buildear el dockerfile
```sh
docker build -f ./build/Dockerfile -t idatos .
```
2. Crear el contenedor con la carpeta compartida del código
```sh
docker run --name idatos -v [IDATOS_FOLDER_PATH]:/code -it [IMAGE_ID|IMAGE_NAME]
```

### Ejemplo:
```sh
docker run --name idatos -v /home/user/IDatos:/code -it idatos
```

***Verificar que en la carpeta "/code" dentro del contenedor se encuentra el código***

## Pasos a seguir para instalar la base de datos

1. sudo apt update
2. sudo apt install postgresql postgresql-contrib -y
3. sudo service postgresql status
4. sudo -i -u postgres (Cambia al usuario de postgres)
5. psql (Accede al PostgreSQL prompt) // Aca la idea va a ser crear un script para crear las BD y poder levantarla todos igual

### Instalando pgAdmin

1. Instalarlo en windows para poder visualizar las tablas.

## Comandos utiles:

Para inicializar el docker e iniciarlo
```sh
docker start idatos
docker exec -it idatos /bin/bash
```

Ejecución del producto dentro del docker:

```sh
cd /code
python3 IDatos.py "[elemento]" [PESO_EN_GRAMOS]
```
Por ejemplo:
```sh
python3 IDatos.py "iphone 12 pro" 189
```

## Provenance de los datos

1. Origen de los datos: Los datos se obtienen de las APIs de MercadoLibre, eBay y PuntoMio.
2. Transformaciones Aplicadas:
   1. find_word: Se realiza un filtrado para no ingresar resultados que no contengan el elemento a buscar dentro del título.
   2. insert_busqueda: Se realiza un mapeo de los datos obtenidos por las APIs a un esquema de base de datos.
3. Diccionario semántico:
   1. title: Titulo de la búsqueda
   2. price: Precio del articulo
   3. currency_id: Moneda referente al precio
   4. URL: URL del elemento dentro del sitio web