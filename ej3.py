nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes?")
aficiones = "Nadar", "Correr", "Leer"


def presentar_persona(nombre="Usuario", edad=None, *aficiones):
	print(f"Hola {nombre}, tu edad es {edad} y tus aficiones son: {aficiones},")
presentar_persona( nombre, edad, *aficiones)

