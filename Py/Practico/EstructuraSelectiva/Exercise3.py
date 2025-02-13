# Determine si un año dado es bisiesto. Un año es bisiesto si
# es divisible por 4, pero no por 100, a menos que también sea divisible por 400.

age = int(input("Ingrese el año a validar: "))

divisibleFor = age % 4 == 0
notDivisibleOneHundred = age % 100 != 0
divisibleForHundred = age % 400 == 0

if divisibleFor and notDivisibleOneHundred or divisibleForHundred:
    print(f"El año {age} es bisiesto.")
else:
    print(f"El año {age} no es bisiesto.")
