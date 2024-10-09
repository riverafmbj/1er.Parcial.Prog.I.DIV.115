from validaciones import *

def menu()->str:
  """
  Imprime el menú en pantalla

  Returns:
      input: para seleccionar la opción que querramos
  """
  print(f"{'CLÍNICA LA FUERZA':^50}")
  print(f"{'Sistema de Gestión de Clínica':^50}")
  print("1 - Cargar pacientes")
  print("2 - Mostrar todos los pacientes")
  print("3 - Buscar pacientes por número de historia clínica")
  print("4 - Ordenar pacientes por número de historia clínica")
  print("5 - Mostrar pacientes con mas días de internación")
  print("6 - Mostrar pacientes con menos días de internación")
  print("7 - Cantidad de pacientes con mas de 5 días de internación")
  print("8 - Promedio de días de internación de todos los pacientes")
  print("9 - Salir")

  return input("Ingrese opción: ")

def agregar_paciente()->list:
  """
  Crea una lista con el número de historia clínica, nombre, 
  edad, diagnóstico y cantidad de días de internación del paciente

  Returns:
      (list): La lista con los datos del paciente
  """
  nuevo_paciente = []
  
  historia_clinica = input("Ingrese el número de historia clinica del paciente: ")
  nuevo_paciente.append(validar_entero(historia_clinica))

  nombre = input("Ingrese nombre del paciente: ")
  nuevo_paciente.append(validar_string(nombre).title())
  
  edad = input("Ingrese la edad del paciente: ")
  nuevo_paciente.append(validar_entero(edad))

  diagnostico = input("Ingrese el diagnóstico del paciente: ")
  nuevo_paciente.append(validar_string(diagnostico).capitalize())

  dias_internacion = input("Ingrese la cantidad de dias internacion: ")
  nuevo_paciente.append(validar_entero(dias_internacion))

  return nuevo_paciente

def mostrar_pacientes(lista_pacientes:list) -> None:
  """
  Imprime por pantalla los datos de todos los pacientes

  Args:
      lista_pacientes(list): la lista de los pacientes
  Returns:
      None
  """   
  if lista_pacientes == []:
    print("No hay pacientes.")
  
  else:
    print(f" {'LISTADO DE PACIENTES':^65} ")
    print(f"{'Historia clínica':^30} {'Nombre y apellido':^25} {'Edad':^15} {'Diagnóstico':^15} {'Días internado/a':^20}")
    print("-----------------------------------------------------------------------------------------------------------------")
    for paciente in lista_pacientes:
      for _ in paciente:
        historia_clinica = paciente[0]
        nombre = paciente[1]
        edad = paciente[2]
        diagnostico = paciente[3]
        dias_internacion = paciente[4]
      print(f"{historia_clinica:^30} {nombre:^25} {edad:^15} {diagnostico:^15} {dias_internacion:^20}")
    print("-----------------------------------------------------------------------------------------------------------------")

def buscar_pacientes(lista_pacientes:list, historia_clinica:int) -> None:
  """
  Busca por número de historia clínica e imprime por pantalla los datos de un paciente

  Args:
      lista_pacientes(list): la lista en la cual se busca el paciente
      historia_clinica(int): el número de historia clínica del paciente que queremos buscar
  Returns:
      None
  """
  if lista_pacientes == []:
    print("No hay pacientes.")
  
  else: 
    for paciente in lista_pacientes:
      if paciente[0] == historia_clinica:
        historia_clinica == paciente[0]
        nombre = paciente[1]
        edad = paciente[2]
        diagnostico = paciente[3]
        dias_internacion = paciente[4]
        print("----------------------------------------------------------------------------------------------")
        print(f"Número de historia clínica: {historia_clinica} - Nombre: {nombre} - Edad: {edad} - Diagnóstico: {diagnostico} - Días de internación: {dias_internacion}")
        print("---------------------------------------------------------------------------------------------")
        break
      else:
        print("---------------------------------------------------------------------------------------------")
        print("El número de historia clínica no coincide con el de ningún paciente")
        print("---------------------------------------------------------------------------------------------")

def ordenar_paciente_ascendente(lista_pacientes:list) -> None:
  """
  Ordena la lista de pacientes por número de historia clínica ascendente

  Args:
      lista_pacientes(list): la lista de pacientes
  Returns:
      None
  """
  if lista_pacientes == []:
    print("No hay pacientes.")
  else:
    longitud = len(lista_pacientes)

    for i in range(longitud):
      for j in range(longitud - 1 - i):
        if lista_pacientes[j][0] > lista_pacientes[j+1][0]:
          aux = lista_pacientes[j+1]
          lista_pacientes[j+1] = lista_pacientes[j]
          lista_pacientes[j] = aux

def buscar_paciente_mas_internado(lista_pacientes: list) -> None:
  """
  Busca e imprime por pantalla los datos del paciente con mas días de internación de la lista de pacientes

  Args:
      lista_pacientes(list): la lista en la cual se busca el paciente con mas días de internación
  
  Returns:
      None
  """     
  if lista_pacientes == []:
    print("No hay pacientes.")
  else:
    dias_paciente_mas_internado = 0

    for paciente in lista_pacientes:
      dias_internacion = paciente[4]
      if dias_internacion > dias_paciente_mas_internado:
        dias_paciente_mas_internado = dias_internacion
        

    for paciente in lista_pacientes:
      if paciente[4] == dias_paciente_mas_internado:
        historia_clinica = paciente[0]
        nombre = paciente[1]
        edad = paciente[2]
        diagnostico = paciente[3]
        dias_internacion = paciente[4]   
        print(f"Número de historia clínica: {historia_clinica} - Nombre: {nombre} - Edad: {edad} - Diagnóstico: {diagnostico} - Días de internación: {dias_internacion}")


def buscar_paciente_menos_internado(lista_pacientes: list) -> None:
  """
  Busca e imprime por pantalla los datos del paciente con menos días de internación de la lista de pacientes

  Args:
      lista_pacientes(list): la lista en la cual se busca el paciente con menos días de internación
  
  Returns:
      None
  """     
  if lista_pacientes == []:
    print("No hay pacientes.")
  else:
    dias_paciente_menos_internado = 0
    flag_dias_menos_internado = False

    for paciente in lista_pacientes:
      dias_internacion = paciente[4]
      if flag_dias_menos_internado == False or dias_internacion < dias_paciente_menos_internado:
        dias_paciente_menos_internado = dias_internacion
        flag_dias_menos_internado = True
        

    for paciente in lista_pacientes:
      if paciente[4] == dias_paciente_menos_internado:
        historia_clinica = paciente[0]
        nombre = paciente[1]
        edad = paciente[2]
        diagnostico = paciente[3]
        dias_internacion = paciente[4]   
        print(f"Número de historia clínica: {historia_clinica} - Nombre: {nombre} - Edad: {edad} - Diagnóstico: {diagnostico} - Días de internación: {dias_internacion}")


def contar_pacientes(lista_pacientes:list) -> None:
  """
  Cuenta en imprime por pantalla la cantidad de pacientes con mas de 5 días de internación si es que los hay

  Args:
      lista_pacientes(list): la lista de pacientes
  Returns:
      None
  """       
  if lista_pacientes == []:
    print("No hay pacientes.")
  else:
    contador = 0
    for paciente in lista_pacientes:
      dias_internacion = paciente[4]
      if dias_internacion > 5:
        contador += 1
    if contador == 0:
      print("No hay pacientes con mas de 5 días de internación")
    else:
      print(f"Hay {contador} pacientes con mas de 5 días de internación")

def calcular_promedio_dias_internacion(lista_pacientes:list) -> None:
  """
  Calcula el promedio de los días de internación de todos los pacientes, si es que los hay

  Args:
      lista_pacientes(list): la lista de pacientes
  Returns:
      promedio(float) or None: Devuelve el promedio(float) si es que hay pacientes en la lista. Devuelve None si no hay pacientes.
  """  
  if lista_pacientes == []:
    print("No hay pacientes.")
  else:
    acumulador = 0
    for paciente in lista_pacientes:
      dias_internacion = paciente[4]
      acumulador += dias_internacion

    promedio = acumulador / len(lista_pacientes)
    print(f"El promedio de la cantidad de días de internación de todos los pacientes es de {promedio} días")