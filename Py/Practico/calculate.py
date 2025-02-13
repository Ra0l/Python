# Realizar una calculadora ingresando numero y digitando el tipo de operación,
# que tenga la opción salir para terminar dicho programa.
print("Bienvendios a la calculadora conti")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y divi")

result = ""
while True:
    if not result:
        result = input("Ingrese número: ")
        if result.lower() == "Salir":
            break
        result = int(result)
    op = input("Ingresa operación: ")
    if op.lower() == "Salir":
        break
    n2 = input("Ingrese siguiente número: ")
    if n2.lower() == "Salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        result += n2
    elif op.lower() == "resta":
        result -= n2
    elif op.lower() == "multi":
        result *= n2
    elif op.lower() == "div":
        result /= n2
    else:
        print("Operación no valida")
        break
    print(f"El resultado es {float(result)}")
