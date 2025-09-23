"""Pedimos los datos al usuario"""
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuál es tu altura en metros? "))
""""Mostramos los datos por pantalla"""
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")
"""Vemos el tipo de dato de cada variable"""
print(type(nombre))
print(type(edad))
print(type(altura))
