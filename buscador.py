def buscar_paciente_por_hc(pacientes : list):
    paciente_buscado = int(input("Ingrese el numero de H.C. del paciente a buscar : "))
    se_encontro = False
    for i in range (len(pacientes)):
        if pacientes[i][0] == paciente_buscado :
            print("El paciente con el numero de H.C. buscado es: ")
            mostrar_paciente(pacientes[i])
            se_encontro = True
            break
    if not se_encontro:
        print("No se encontro el paciente")