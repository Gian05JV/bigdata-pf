'''Instalar
pip install pymongo
pip install certifi
pip installl pymongo[srv]
'''

from pymongo import MongoClient

client = MongoClient('mongodb://192.168.0.13:27017/')

def dbConexion():
    try:

        client = MongoClient('mongodb://192.168.0.13:27017/')
        db = client['dbisesion']
    except ConnectionError:
        print("Error al conectar a la bd")
    return db

def consulta_sensores():
    #crea una nueva cinexion a la bd
    db = dbConexion()
    #entramos a la coleccion de la bd llamada sensores
    usuarios = db['words']
    #obtenemos todos los documentos de la coleccion sensores
    c_usuarios = usuarios.find()
    #retornamos la consulta
    return c_usuarios

if __name__ == '__main__':
    base = dbConexion()

