from pymongo import MongoClient
from bson import ObjectId
import os


class MongoDB():
    def __init__(self) -> None:
        mongo                = MongoClient(os.getenv('MONGO_CONNECTION_STRING'))
        self.mongo_db_movies = mongo.db.movies

    def insert_one(self, movie:dict) -> dict:
        inserted_movie = self.mongo_db_movies.insert_one(movie)
        movie.pop('_id')
        movie['id'] = str(inserted_movie.inserted_id)
        return movie

    def find_one(self, id:str) -> dict:
        found_movie = self.mongo_db_movies.find_one({"_id":ObjectId(id)})
        if not found_movie: return None
        movie:dict = {
            "id": id,
            "name": found_movie['name'],
            "year": found_movie['year'],
        }
        return movie
    
    def find(self) -> list[dict]:
        mongo_movies = list(self.mongo_db_movies.find())
        movies = list(map(lambda mongo_movie: {
            "id": str(mongo_movie['_id']),
            "name": mongo_movie['name'],
            "year": mongo_movie['year'],
        }, mongo_movies))
        return movies