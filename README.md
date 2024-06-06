## Puesta en marcha Manual
### Prerequisites:
* [GitHub](https://git-scm.com/)
* [Brew](https://brew.sh/#install)
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
* [Python 3.12.3](https://www.python.org/ftp/python/3.12.3/python-3.12.3-macos11.pkg)
* [Mongo 7.0](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)
    ```bash
    brew tap mongodb/brew
    brew update
    brew install mongodb-community@7.0
    ```
* .env
    ```bash
    MONGO_CONNECTION_STRING=mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.6
    ```

### Getting Started:
```bash
# Start MongoDB
brew services start mongodb/brew/mongodb-community
# Start API
git clone https://github.com/jmfigue6/python-mongo-api.git
cd python-mongo-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
---
## Puesta en marcha Docker
La idea es dockerizar el proyecto tanto para ahorrarse todos los pasos manuales anteriores como para luego poder escalar los servicios con Kubernetes.  Para esto me gustaría cubrir:
* Utilizar variable de entorno dentro en Dockerfile y Docker-Compose
* Creación de Network (que no se pueda acceder al contenedor de mongo desde afuera?)
* Ejecución ejemplo con y sin Volume
* Ejemplo para cuando se inicialice el contenedor cree la DB y la tabla, incluso tener una alguna carga inicial
* Y finalmente, entender escalado de instancias de cada contenedor .. sobre todo del contenedor de la DB que va a apuntar a un mismo volumen (se escalaría la instancia .. quedando todas apuntando a la misma carpeta del disco rígido)

### Prerequisites:
* [GitHub](https://git-scm.com/)
* [Docker](https://docs.docker.com/desktop/)

### Getting Started:
```bash
git clone https://github.com/jmfigue6/python-mongo-api.git
cd python-mongo-api
# Estos comandos aún no se pueden ejecutar, hay que dockerizar primero!
docker build -t python-mongo-api-docker-image:latest .
docker-compose up
```

---
### Ready to use:
```bash
curl http://127.0.0.1:9090/movie -v -XPOST -d '{
    "name": "Back to the Future",
    "year": 1985
}'

curl http://127.0.0.1:9090/movies

curl http://127.0.0.1:9090/movie/{movie_id}
```

---
#### MongoDB Tutoriales
* [Complete MongoDB Tutorial](https://www.youtube.com/playlist?list=PL4cUxeGkcC9h77dJ-QJlwGlZlTd4ecZOA)
* [Install mongoDB and MongoDB Compass on Mac](https://www.youtube.com/watch?v=MyIiM7z_j_Y)
* [MongoDB Compass Download (GUI)](https://www.mongodb.com/try/download/compass)