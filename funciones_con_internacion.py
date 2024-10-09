from funciones_del_paciente import *
def mostrar_paciente_con_mas_dias_internacion(pacientes : list):
    mayor_dia = pacientes[0][4]
    paciente = pacientes[0]
    for i in range (len(pacientes)):
        if pacientes[i][4] > mayor_dia:
            mayor_dia = pacientes[i][4]
            paciente = pacientes[i]
    mostrar_paciente(paciente)

def mostrar_paciente_con_menos_dias_internacion(pacientes : list):
    menor_dia = pacientes[0][4]
    paciente = pacientes[0]
    for i in range (len(pacientes)):
        if pacientes[i][4] < menor_dia:
            menor_dia = pacientes[i][4]
            paciente = pacientes[i]
    mostrar_paciente(paciente)
    
def cantidad_pacientes_mas_de_5_dias_internacion(pacientes : list):
    DIAS = 5
    contador = 0
    for i in range (len(pacientes)):
        if pacientes[i][4] > DIAS:
            contador += 1
    print(f"La cantidad de paciente con mas de 5 dias de internacion es : {contador}")
    
def calcular_promedio_dias_internacion_total_pacientes(pacientes : list):
    sumador_dias = 0
    cant_pacientes = len(pacientes)
    for i in range(cant_pacientes):
        sumador_dias += pacientes[i][4]
    promedio = sumador_dias / cant_pacientes
    return promedio