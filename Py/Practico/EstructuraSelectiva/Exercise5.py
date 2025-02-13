# Entrada de datos
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

mayor = 0

if num1 > num2 and num1 > num3:
    mayor = num1
    print(mayor)
elif num2 > num1 and num2 > num3:
    mayor = num2
    print(mayor)
else:
    mayor = num3
    print(mayor)

# Llamada a la función y mostrar el mayor número
print(f"El número mayor es: {mayor}")
