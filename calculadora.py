import sys

def main():
    # sys.argv es una lista con los argumentos de la línea de comandos
    # El primer elemento (posición 0) es siempre el nombre del archivo
    print("Argumentos recibidos:", sys.argv)

    # Si hay argumentos adicionales, los mostramos
    if len(sys.argv) > 3:
        num1 = sys.argv[1]
        operador = sys.argv[2]
        num2 = sys.argv[3]
        try:
            num1 = float(num1)
            num2 = float(num2)
            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Error: División por cero.")
                    return
            else:
                print(f"Operador no reconocido: {operador}")
                return
            print(f"{num1} {operador} {num2}: {resultado}")
        except ValueError:
            print("Error: Los argumentos deben ser números válidos.")
            return
    else:
        print("No se proporcionó los argumentos necesarios. Uso: python calculadora.py <num1> <operador> <num2>")

if __name__ == "__main__":
    main()