# Función para calcular el porcentaje de faltas
def calcular_porcentaje_faltas(faltas_asignaturas, horas_asignaturas):
    # Calcula el porcentaje de faltas para cada asignatura
    porcentaje_faltas = {asignatura: (faltas / horas) * 100 for asignatura, faltas, horas in zip(faltas_asignaturas.keys(), faltas_asignaturas.values(), horas_asignaturas.values())}
    return porcentaje_faltas

# Función para calcular las faltas restantes hasta el 15%
def calcular_faltas_restantes(faltas_asignaturas, horas_asignaturas):
    # Calcula las faltas restantes hasta el 15% para cada asignatura
    faltas_restantes = {asignatura: int(horas * 0.15) - faltas for asignatura, faltas, horas in zip(faltas_asignaturas.keys(), faltas_asignaturas.values(), horas_asignaturas.values())}
    return faltas_restantes

# Función para calcular el valor del porcentaje de cada falta según la asignatura
def calcular_valor_porcentaje_falta(faltas_asignaturas, horas_asignaturas):
    # Calcula el valor del porcentaje de cada falta según la asignatura
    valor_porcentaje_falta = {asignatura: (1 / horas) * 100 for asignatura, horas in zip(horas_asignaturas.keys(), horas_asignaturas.values())}
    return valor_porcentaje_falta

