# Importa las funciones necesarias de otros módulos
from asistencia import leer_asistencia, procesar_asistencia
from calculos import calcular_porcentaje_faltas, calcular_faltas_restantes, calcular_valor_porcentaje_falta
from archivo import escribir_json

def main():
    # Define las horas totales para cada asignatura
    horas_asignaturas = {
        'Desarrollo web en entorno cliente': 125,
        'Desarrollo web en entorno servidor': 160,
        'Despliegue de aplicaciones web': 90,
        'Diseño de interfaces web': 165,
        'Empresa e iniciativa emprendedora': 60,
        'Proyecto de Desarrollo de Aplicaciones Web': 40
    }
    # Inicializa el conteo de faltas para cada asignatura a 0
    faltas_asignaturas = {asignatura: 0 for asignatura in horas_asignaturas.keys()}
    # Lee los datos de asistencia
    data = leer_asistencia()
    # Procesa los datos de asistencia
    asistencia_data = procesar_asistencia(data, faltas_asignaturas)
    # Calcula el porcentaje de faltas para cada asignatura
    porcentaje_faltas = calcular_porcentaje_faltas(faltas_asignaturas, horas_asignaturas)
    # Calcula las faltas restantes hasta el 15% para cada asignatura
    faltas_restantes = calcular_faltas_restantes(faltas_asignaturas, horas_asignaturas)
    # Calcula el valor del porcentaje de cada falta según la asignatura
    valor_porcentaje_falta = calcular_valor_porcentaje_falta(faltas_asignaturas, horas_asignaturas)
    # Escribe los datos procesados en un archivo JSON
    escribir_json(asistencia_data, faltas_asignaturas, porcentaje_faltas, faltas_restantes, valor_porcentaje_falta)
    print("Archivo JSON generado con éxito: 'asistencia.json'")

# Comprueba si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
