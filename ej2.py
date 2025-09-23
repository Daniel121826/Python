nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuál es tu altura en metros? "))
peso = float(input("¿Cuál es tu peso en kg? "))
"""Hacemos la función saludar"""
def saludar(nombre:str):
    return print(f"Hola {nombre})")

    saludar(nombre)

def calcular_imc(peso:float, altura:float)->float:
    imc = peso / (altura ** 2)
    return print(f"Tu imc es: {imc:.2f}")

calcular_imc(peso, altura)