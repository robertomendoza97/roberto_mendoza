import math

def calcularDescuentoEntradas(cantidadDeEntradas):

  precioBase = 10

  precioTotal = 0

  if cantidadDeEntradas >= 5: 
    precioTotal = (precioBase * cantidadDeEntradas) * 0.75
  elif cantidadDeEntradas >= 3: 
    precioTotal = (precioBase * cantidadDeEntradas) * 0.85
  else: 
    precioTotal = precioBase * cantidadDeEntradas
  
  print(f"El precio total de las entradas es de: {precioTotal} \n")
  input("presiona enter para continuar...")

def calcularTrianguloEquilatero(lado): 
  area = (math.sqrt(3) * lado * lado )  / 4

  print(f"El area del triangulo equilatero es: {area} \n")
  input("presiona enter para continuar...")

def mostrarMenu():
  ejecutar = True

  while ejecutar: 
    print("Powered by @Pingüe Soft \n")
    print("¡Bienvenido! Elige una opcion.")
    print("1-) Comprar entradas de cine.")
    print("2-) Calcular area de triangulo equilátero.")
    print("3-) Salir.")

    eleccion = input("\n")

    if eleccion == "1" :
      cant = int(input("Cuantas entradas quieres? "))
      calcularDescuentoEntradas(cant)
    elif eleccion == "2": 
      lado = int(input("Cual es la medida del lateral del triangulo (cm)? "))
      calcularTrianguloEquilatero(lado)
    elif eleccion == "3":
      print("Hasta luego.")
      ejecutar = False
    else: 
      print("Opcion no disponible \n")

mostrarMenu()