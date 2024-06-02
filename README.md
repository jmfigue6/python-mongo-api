## ENV
MONGO_CONNECTION_STRING

## Python
https://www.python.org/downloads/
* Install
```bash
https://www.python.org/downloads/
ln -s -f /usr/local/bin/python3 /usr/local/bin/python
python -m venv venv
source venv/bin/activate
```
* Dependencies
```bash
pip install flask
pip install pymongo

pip freeze > requirements.txt
pip install -r requirements.txt
```

## MongoDB
[Complete MongoDB Tutorial](https://www.youtube.com/playlist?list=PL4cUxeGkcC9h77dJ-QJlwGlZlTd4ecZOA)
[Install mongoDB and MongoDB Compass on Mac](https://www.youtube.com/watch?v=MyIiM7z_j_Y)
[install-mongodb-on-os-x](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)
[MongoDB Compass Download (GUI)
](https://www.mongodb.com/try/download/compass)
* Install
```bash
brew tap mongodb/brew
brew update
brew install mongodb-community@7.0
```
* Start
```bash
mongod --version
brew services start mongodb/brew/mongodb-community
```
* DB/Table creation from UI
```bash
db.movies
```
