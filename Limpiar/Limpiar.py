from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/diccionariojuridico")
db = client["diccionariojuridico"]

result = db.terminos.delete_many({})
print(f"✅ Se eliminaron {result.deleted_count} documentos de la colección 'terminos'.")
