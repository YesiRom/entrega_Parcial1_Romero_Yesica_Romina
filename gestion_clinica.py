from menu import *
from funciones_del_paciente import *
from carga_de_pacientes import *
from buscador import *
from ordenamiento import *
from funciones_con_internacion import *
from parcial import *

pacientes = []
TERMINAR = ""
alumna()
while TERMINAR != "salir":
    mostrar_menu_principal()
    opcion = int(input("elegir la opcion de menu: "))
        
    match opcion:
        case 1:
            cargar_paciente(pacientes)
        case 2:
            mostrar_pacientes(pacientes)
        case 3:
            buscar_paciente_por_hc(pacientes)
        case 4:
            ordenar_paciente_por_hc(pacientes)
        case 5:
            mostrar_paciente_con_mas_dias_internacion(pacientes)
        case 6:
            mostrar_paciente_con_menos_dias_internacion(pacientes)
        case 7:
            cantidad_pacientes_mas_de_5_dias_internacion(pacientes)
        case 8:
            promedio = int(calcular_promedio_dias_internacion_total_pacientes(pacientes))
            print(f"El promedio de dias de internacion de todos los pacientes es: {promedio}")
        case 9:
            TERMINAR = "salir"
print ("Saliendo del sistema.... hasta pronto!")