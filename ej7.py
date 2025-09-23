
numeros = input("Introduce una lista de números separados por comas: ")
numeros_lista = numeros.split(",")
numeros_lista = [int(num) for num in numeros_lista]
suma = sum(numeros_lista)
promedio = suma / len(numeros_lista)
maximo = max(numeros_lista)
minimo = min(numeros_lista)
print(f"Suma: {suma}, Promedio: {promedio}, Máximo: {maximo}, Mínimo: {minimo}")