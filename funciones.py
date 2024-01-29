import json

class Funciones():

    def obtener_data():
        with open('data.json') as f:
            data = json.load(f)
        return data

    def guardar_data(data):
        with open('data.json', 'w') as f:
            json.dump(data, f)

    

