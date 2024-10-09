def cargar_paciente(pacientes : list):
    n= int(input("ingrese la cantidad de pacientes a agregar: "))
    
    for _ in range(n):
        historia_clinica = int(input("Ingrese el número de historia clinica del paciente: "))
        nombre = input("Nombre : ")
        edad = int(input("Edad : "))
        diagnostico = input("Diagnostico")
        dias_internacion = int(input("Cantidad de dias de internacion:  : "))
        paciente =[historia_clinica, nombre, edad, diagnostico, dias_internacion]
        pacientes += [paciente]
    return pacientes