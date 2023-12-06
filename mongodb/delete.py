from conexion import conectar

def eliminar_por_fecha(fecha):
    try:
        coleccion = conectar()
        coleccion.delete_many({"Fecha": fecha})
        print("Datos eliminados correctamente.")
    except Exception as e:
        print("Error al eliminar datos:", e)
