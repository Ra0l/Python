# 4: Pide al usuario ingresar una lista de números y cuenta cuántos son pares e impares.

# Función para contar números pares e impares
def contar_pares_impares(lista_numeros):
    pares = 0
    impares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


# Entrada de datos
numeros = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada en una lista de enteros
lista_numeros = list(map(int, numeros.split()))

# Contar pares e impares
pares, impares = contar_pares_impares(lista_numeros)

# Mostrar el resultado
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
