from funciones import *
from validaciones import *

pacientes = []

respuesta = "no"
while respuesta == "no":
  match menu():
    case "1":
      pacientes.append(agregar_paciente())
      continuar = input("¿Desea agregar otro paciente?: ")
      while continuar == "si":
        pacientes.append(agregar_paciente())
        continuar = input("¿Desea agregar otro paciente?: ")
      
    case "2":
      mostrar_pacientes(pacientes)

    case "3":
      if pacientes == []:
        print("No hay pacientes.")  
      else:
        paciente_a_buscar = input("Ingrese el número de historia clínica del paciente a buscar: ")
        buscar_pacientes(pacientes, validar_entero(paciente_a_buscar))

    case "4":
      ordenar_paciente_ascendente(pacientes)
      for paciente in pacientes:
          for _ in paciente:
            historia_clinica = paciente[0]
            nombre = paciente[1]
            edad = paciente[2]
            diagnostico = paciente[3]
            dias_internacion = paciente[4]
          print(f"Número de historia clínica: {historia_clinica} - Nombre: {nombre} - Edad: {edad} - Diagnóstico: {diagnostico} - Días de internación: {dias_internacion}")

    case "5":
      buscar_paciente_mas_internado(pacientes)

    case "6":
      buscar_paciente_menos_internado(pacientes)

    case "7":
      contar_pacientes(pacientes)

    case "8":
      calcular_promedio_dias_internacion(pacientes)

    case "9":
      respuesta = input("¿Está seguro que desea salir? (si/no): ")
      while respuesta != "no" and respuesta != "si":
        respuesta = input("Error. Ingrese 'si' o 'no' : ")

    case _:
      print("Error. Ingrese una opción correcta. (De 1 a 9)")