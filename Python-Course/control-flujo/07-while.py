numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2
#     print("numero: ", numero)


while True:  # Mientras comando sea diferente de "salir" se ejecutará el bloque de código
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
