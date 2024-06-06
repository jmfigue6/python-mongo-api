from flask import Flask, request, jsonify
from mongodb import MongoDB

app = Flask (__name__)
mongodb = MongoDB()

@app.route("/movie", methods=["POST"])
def create_movie():
    movie:dict = request.get_json()
    inserted_movie = mongodb.insert_one(movie)
    return jsonify(inserted_movie)

@app.route("/movie/<id>", methods=["GET"])
def get_movie(id:str):
    found_movie = mongodb.find_one(id)
    if not found_movie: return not_found()
    return jsonify(found_movie)

@app.route("/movies", methods=["GET"])
def all_movies():
    mongo_movies = mongodb.find()
    return jsonify(mongo_movies)

@app.errorhandler(404)
def not_found():
    response = jsonify({
        'message': 'Not Found:' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(debug=True, port=9090)