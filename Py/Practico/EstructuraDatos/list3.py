notas_user = []
contador = 0
while contador < 2:
    notas = float(input("Ingrese la nota: "))
    notas_user.append(notas)
    # promedio
    suma_total = sum(notas_user)
    cant_valores = len(notas_user)

    promedio = suma_total / cant_valores

    contador += 1

print("Notas: ", notas_user)
print("El promedio es: ", promedio)
