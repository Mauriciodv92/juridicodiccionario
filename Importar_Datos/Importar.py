from pymongo import MongoClient

# === Configuración MongoDB ===
MONGO_URI = "mongodb://mongo:27017/diccionariojuridico"
DB_NAME = "diccionariojuridico"
COLLECTION_NAME = "terminos"

# === Conectar a la base de datos ===
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
coleccion = db[COLLECTION_NAME]

# === Leer archivo txt ===
terminos = []
with open("terminos_juridicos_colombianos_100.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().strip()
    bloques = contenido.split("\n\n")
    for bloque in bloques:
        lineas = bloque.strip().split("\n", 1)
        if len(lineas) == 2:
            termino = lineas[0].strip().title()
            descripcion = lineas[1].strip()
            if termino and descripcion:
                terminos.append({"termino": termino, "descripcion": descripcion})

# === Insertar en la colección ===
if terminos:
    coleccion.insert_many(terminos)
    print(f"✅ Se insertaron {len(terminos)} términos correctamente en la base de datos.")
else:
    print("⚠️ No se encontraron términos válidos en el archivo.")
