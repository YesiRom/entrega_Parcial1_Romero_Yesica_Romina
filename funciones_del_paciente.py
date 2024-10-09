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

def mostrar_pacientes(pacientes : list):
    for i in range(len(pacientes)):
        print( pacientes[i])

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

    

def ordenar_paciente_por_hc(pacientes: list):
    longitud = len(pacientes)
    
    for i in range(longitud):
        for j in range(longitud - 1 -i):
            if pacientes[j][0] > pacientes[j +1][0]:
                temporal = pacientes[j + 1]
                pacientes[j +1] = pacientes[j]
                pacientes[j] = temporal
    mostrar_pacientes(pacientes)

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

def mostrar_paciente(paciente : list):
        print(f"H.C. : {paciente[0]}, Nombre : {paciente[1]}, Edad : {paciente[2]}, Diagnostico : {paciente[3]}, Cantidad de dias de internacion : {paciente[4]}")