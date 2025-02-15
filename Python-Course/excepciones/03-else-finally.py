try:
    n1 = int(input("Ingresa primer número: "))
except:
    print("Ocurrio un error!")
else:
    print("No ocurrio ningun error")
finally:
    print("se ejecuta siempre")
