print("Bienvenido a la calculadora")
print("Para salir escribe 'salir'")
print("Operaciones disponibles: suma, resta, multiplicacion, division")

resultado = ""

while True:
    if not resultado:
        resultado = input("Introduce un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa la operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print("Operación no válida")
        break

    print(f"Resultado: {resultado}")
