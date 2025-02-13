lista_user_numbers = []
contador = 0
contador_pos = 0
contador_neg = 0

print("Ingrese 5 numeros enteros")
while contador < 5:
    number = int(input("ingrese valor: "))
    lista_user_numbers.append(number)

    if number % 2 == 0:
        contador_pos = contador_pos + 1
    else:
        contador_neg += 1

    contador += 1

print("lista = ", lista_user_numbers)

print("pares: ", contador_pos)
print("impares: ", contador_neg)
