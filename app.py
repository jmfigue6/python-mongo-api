from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os

app                     = Flask (__name__)
mongo                   = MongoClient(os.getenv('MONGO_CONNECTION_STRING'))
mongo_db_movies         = mongo.db.movies

@app.route("/movie", methods=["POST"])
def create_movie():
    movie:dict = request.get_json()
    inserted_movie = mongo_db_movies.insert_one(movie)
    movie.pop('_id')
    movie['id'] = str(inserted_movie.inserted_id)
    return jsonify(movie)

@app.route("/movie/<id>", methods=["GET"])
def get_movie(id:str):
    found_movie = mongo_db_movies.find_one({"_id":ObjectId(id)})
    if not found_movie: return not_found()
    movie:dict = {
        "id": id,
        "name": found_movie['name'],
        "year": found_movie['year'],
    }
    return jsonify(movie)

@app.route("/movies", methods=["GET"])
def all_movies():
    mongo_movies = list(mongo_db_movies.find())
    movies = list(map(lambda mongo_movie: {
        "id": str(mongo_movie['_id']),
        "name": mongo_movie['name'],
        "year": mongo_movie['year'],
    }, mongo_movies))
    return jsonify(movies)

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(debug=True, port=9090)