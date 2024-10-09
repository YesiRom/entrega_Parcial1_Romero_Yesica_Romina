def mostrar_pacientes(pacientes : list):
    for i in range(len(pacientes)):
        print( pacientes[i])


def mostrar_paciente(paciente : list):
        print(f"H.C. : {paciente[0]}, Nombre : {paciente[1]}, Edad : {paciente[2]}, Diagnostico : {paciente[3]}, Cantidad de dias de internacion : {paciente[4]}")