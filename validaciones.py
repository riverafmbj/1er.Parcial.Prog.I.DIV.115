def validar_entero(entero:str) -> int:
  """
  Valida que el entero sea un digito

  Args:
      entero(str): el entero a validar
  
  Returns:
      entero(int): devuelve el entero validado
  """   
  while not entero.isdigit() or int(entero) <= 0:
      entero = input(f"Error. Ingrese el dato correctamente: ")
  return int(entero)

def validar_string(string:str) -> int:
  """
  Valida que el string sea un digito

  Args:
      string(str): el string a validar
  
  Returns:
      string(int): devuelve el string validado
  """

  while string.isdigit() or string.strip() == "":
    string = input(f"Error. Ingrese el dato correctamente: ")
  return string