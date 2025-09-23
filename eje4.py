nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
while True:
    try:
        edad = int(edad)
        break
    except ValueError:
        print("Ingrese un número válido para la edad.")
        edad = input("¿Cuántos años tienes? ")

altura = input("¿Cuánto mides (en metros)? ")
while True:
    try:
        altura = float(altura)
        break
    except ValueError:
        print("Por favor, ingresa un número válido para la altura.")
        altura = input("¿Cuánto mides (en metros)? ")
