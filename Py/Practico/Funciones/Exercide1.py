# Funcion para calcular salario
def calculateSalary(hour, tarify):
    salary = hour * tarify
    return salary


hour = float(input("Ingrese el total de horas: "))
tarify = float(input("Ingrese la tarifa a pagar: "))

salaryFinal = calculateSalary(hour, tarify)

print("Su salario es de: S/", salaryFinal, "SOLES")
