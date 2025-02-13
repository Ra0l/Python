# Escribir un programa que pregunte al usuario su renta anual
# y muestre por pantalla el tipo impositivo que le corresponde.

renta_anual = float(input("Ingrese su renta anual en euros: "))
if renta_anual < 1000:
    print(f"Su tipo impositivo es de 5%")
elif renta_anual < 2000:
    print(f"Su tipo impositivo es de 15%")
elif renta_anual < 35000:
    print(f"Su tipo impositivo es de 20%")
elif renta_anual < 60000:
    print(f"Su tipo impositivo es de 30%")
else:
    print(f"Su tipo impositivo es de 45%")
