import emoji

def calcular_imc_con_emoji(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
    elif imc < 25:
        estado = "Normal " + emoji.emojize(":smile:", language="alias")
    else:
        estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
    return imc, estado

imc, estado = calcular_imc_con_emoji(70, 1.75)  # Ejemplo con peso 70kg y altura 1.75m

print(f"Tu IMC es {imc:.2f} → {estado}")
