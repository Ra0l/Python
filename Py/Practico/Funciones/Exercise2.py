# Función para convertir soles a otras monedas
def convertir_monedas(soles, tasa_dolar, tasa_euro, tasa_peso_mexicano):
    dolares = soles * tasa_dolar
    euros = soles * tasa_euro
    pesos_mexicanos = soles * tasa_peso_mexicano
    return dolares, euros, pesos_mexicanos

# Entrada de datos
soles = float(input("Ingrese la cantidad en soles (PEN): "))

# Tasas de cambio (ejemplo ficticio)
tasa_dolar = 0.27  # 1 Sol = 0.27 USD
tasa_euro = 0.25   # 1 Sol = 0.25 EUR
tasa_peso_mexicano = 4.87  # 1 Sol = 4.87 MXN

# Conversión
dolares, euros, pesos_mexicanos = convertir_monedas(soles, tasa_dolar, tasa_euro, tasa_peso_mexicano)

# Mostrar el resultado
print(f"{soles} Soles es equivalente a:")
print(f"{dolares:.2f} Dólares (USD)")
print(f"{euros:.2f} Euros (EUR)")
print(f"{pesos_mexicanos:.2f} Pesos Mexicanos (MXN)")