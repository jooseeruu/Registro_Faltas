import pymongo

def conectar():
    try:
        client = pymongo.MongoClient("mongodb+srv://usuario:contraseña@cluster0.mongodb.net/")
        db = client["registrofaltas"] 
        coleccion = db["asistencia"]
        return coleccion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
