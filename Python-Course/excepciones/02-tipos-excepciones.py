try:
    n1 = int(input("Ingresa primer número: "))
except ValueError as e:
    print("Ingresa un valor que correspond")
except NameError as e:
    print("Ocurrio un error")
