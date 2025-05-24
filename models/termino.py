from flask_pymongo import PyMongo

mongo = PyMongo()


class TerminoModel:
    @staticmethod
    def insertar_termino(termino):
        mongo.db.terminos.insert_one(termino)

    @staticmethod
    def obtener_todos():
        return list(mongo.db.terminos.find().sort("termino", 1))

    @staticmethod
    def obtener_por_id(id):
        from bson.objectid import ObjectId
        return mongo.db.terminos.find_one({'_id': ObjectId(id)})

    @staticmethod
    def actualizar_termino(id, datos):
        from bson.objectid import ObjectId
        mongo.db.terminos.update_one({'_id': ObjectId(id)}, {'$set': datos})

    @staticmethod
    def eliminar_termino(id):
        from bson.objectid import ObjectId
        mongo.db.terminos.delete_one({'_id': ObjectId(id)})

    @staticmethod
    def buscar_terminos(palabra):
        return list(mongo.db.terminos.find({
            '$or': [
                {'termino': {'$regex': palabra, '$options': 'i'}},
                {'descripcion': {'$regex': palabra, '$options': 'i'}}
            ]
        }))
