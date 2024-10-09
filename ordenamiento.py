from funciones_del_paciente import *
def ordenar_paciente_por_hc(pacientes: list):
    longitud = len(pacientes)
    
    for i in range(longitud):
        for j in range(longitud - 1 -i):
            if pacientes[j][0] > pacientes[j +1][0]:
                temporal = pacientes[j + 1]
                pacientes[j +1] = pacientes[j]
                pacientes[j] = temporal
    mostrar_pacientes(pacientes)
