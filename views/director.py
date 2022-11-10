from flask import request
from flask_restx import Resource, Namespace
from container import director_service


directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        """Возвращает список всех режиссеров"""
        directors = director_service.get_all()

        if not directors:
            return "Не найдено", 404

        return directors, 200

    def post(self):
        """Добавляет режиссера"""
        req_json = request.json

        director = director_service.create(req_json)

        return director, 201


@directors_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        """Возвращает подробную информацию о режиссере"""
        director = director_service.get_one(did)

        if not director:
            return "Не найдено", 404

        return director, 200

    def put(self, did):
        """Обновляет режиссера"""

        req_json = request.json
        req_json["id"] = did

        director = director_service.update(req_json)

        if not director:
            return "Не найдено", 404

        return director, 200

    def delete(self, did):
        """Удаляет режиссера"""
        director = director_service.delete(did)

        if not director:
            return "Не найдено", 404

        return director, 200


