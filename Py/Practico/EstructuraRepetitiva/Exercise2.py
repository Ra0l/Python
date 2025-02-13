# Escriba un programa que, dada una lista o tupla de números, determine cuáles son los valores máximos y mínimos.
# Evite hacer uso de las funciones min o max nativas de Python.

# Función para encontrar el valor máximo
def encontrar_maximo(numeros):
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo

# Función para encontrar el valor mínimo


def encontrar_minimo(numeros):
    minimo = numeros[0]
    for numero in numeros:
        if numero < minimo:
            minimo = numero
    return minimo


# Ejemplo de lista o tupla de números
numeros = [15, 22, 8, 31, 13, 7, 40, 25]

# Encontrar el valor máximo y mínimo
maximo = encontrar_maximo(numeros)
minimo = encontrar_minimo(numeros)

# Mostrar los resultados
print(f"El valor máximo es: {maximo}")
print(f"El valor mínimo es: {minimo}")
