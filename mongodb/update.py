from conexion import conectar

def actualizar_asistencia(fecha, nueva_asistencia):
    try:
        coleccion = conectar()
        coleccion.update_many({"Fecha": fecha}, {"$set": nueva_asistencia})
        print("Datos actualizados correctamente.")
    except Exception as e:
        print("Error al actualizar datos:", e)
