import json
from conexion import conectar
import time

coleccion = conectar()

def insertar_datos(datos):
    start_time = time.time()
    try:
        for asistencia in datos["Asistencia"]:
            # Crear un filtro con la fecha, hora de inicio y hora final para comprobar duplicados
            filtro = {
                "Fecha": asistencia["Fecha"],
                "Hora_inicio": asistencia["Hora_inicio"],
                "Hora_fin": asistencia["Hora_fin"]
            }
            # Verificar si el registro ya existe en la base de datos
            if coleccion.count_documents(filtro) == 0:
                coleccion.insert_one(asistencia)
                print(f"Dato para fecha {asistencia['Fecha']}, hora inicio {asistencia['Hora_inicio']} y hora final {asistencia['Hora_fin']} insertado correctamente.")
            else:
                print(f"Dato para fecha {asistencia['Fecha']}, hora inicio {asistencia['Hora_inicio']} y hora final {asistencia['Hora_fin']} ya existe en la base de datos y no se ha insertado.")
    except Exception as e:
        print("Error al insertar datos:", e)
    finally:
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print("Tiempo transcurrido: ", elapsed_time, "milisegundos")

with open('data/asistencia.json') as archivo:
    datos_json = json.load(archivo)

insertar_datos(datos_json)
