from flask import request
from flask_restx import Resource, Namespace
from container import movie_service


movies_ns = Namespace("movies")


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        """
        Возвращает список всех фильмов.
        Можно фильтровать по director_id и/или genre_id
        """
        args = request.args.to_dict()

        movies = movie_service.get_all(args)

        if not movies:
            return "Не найдено", 404

        return movies, 200

    def post(self):
        """Добавляет фильм в фильмотеку"""
        req_json = request.json

        movie = movie_service.create(req_json)

        return movie, 201


@movies_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        """Возвращает подробную информацию о фильме"""
        movie = movie_service.get_one(mid)

        if not movie:
            return "Не найдено", 404

        return movie, 200

    def put(self, mid):
        """Обновляет фильм"""
        req_json = request.json
        req_json["id"] = mid

        movie = movie_service.update(req_json)

        if not movie:
            return "Не найдено", 404

        return movie, 200

    def delete(self, mid):
        """Удаляет фильм"""
        movie = movie_service.delete(mid)

        if not movie:
            return "Не найдено", 404

        return movie, 200
