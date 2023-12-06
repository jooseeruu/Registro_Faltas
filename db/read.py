import pymongo
from conexion import conectar

# Funciones de lectura y ordenación

def buscar_por_fecha(fecha):
    try:
        coleccion = conectar()
        resultados = coleccion.find({"Fecha": fecha})
        for resultado in resultados:
            print(resultado)
    except Exception as e:
        print("Error al buscar por fecha:", e)

def ordenar_por_porcentaje_faltas():
    try:
        coleccion = conectar()
        resultados = coleccion.find().sort("Porcentaje_faltas", pymongo.ASCENDING)
        for resultado in resultados:
            print(resultado)
    except Exception as e:
        print("Error al ordenar por Porcentaje de Faltas:", e)

def ordenar_por_faltas():
    try:
        coleccion = conectar()
        resultados = coleccion.find().sort("Faltas_no_justificadas", pymongo.ASCENDING)
        for resultado in resultados:
            print(resultado)
    except Exception as e:
        print("Error al ordenar por Faltas:", e)

def ordenar_por_faltas_restantes():
    try:
        coleccion = conectar()
        resultados = coleccion.find().sort("Faltas_restantes", pymongo.ASCENDING)
        for resultado in resultados:
            print(resultado)
    except Exception as e:
        print("Error al ordenar por Faltas Restantes:", e)

def ordenar_por_impacto_por_falta():
    try:
        coleccion = conectar()
        resultados = coleccion.find().sort("Valor_porcentaje_falta", pymongo.ASCENDING)
        for resultado in resultados:
            print(resultado)
    except Exception as e:
        print("Error al ordenar por Impacto por Falta:", e)
