# Escribir un programa que lea un entero positivo, n,
# introducido por el usuario y después muestre en pantalla la
# suma de todos los enteros desde 1 hasta n.
# La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma :

# number = int(input("Ingrese numero entero: "))

# plus = number * (number + 1) / 2

# print(f"La suma de numeros enteros de {number} es: {int(plus)}")

# Adicionar: Validar tambien que solo admita numeros enteros y no negativos, ni decimales.

number = int(input("Ingrese numero entero a sumar: "))

if number > 0:
    plus = number * (number + 1) / 2
    print(f"La suma de numeros enteros de {number} es: {int(plus)}")
else:
    print("Ingrese un numero positivo")
