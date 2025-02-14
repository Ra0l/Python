numeros = [8, 45, 7, 13, 9, 3, 2, 11, 0, -1]

# numeros.sort(reverse=True)  # Ordena la lista de mayor a menor
numeros2 = sorted(numeros, reverse=True)  # Ordena la lista de menor a mayor
print(numeros)
print(numeros2)

usuarios = [
    ["chanchito", 5],
    ["gatito", 0],
    ["perrito", 3]
]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
