# set significa grupo o conjunto
# Los sets son colecciones desordenadas de elementos únicos
# Los sets son mutables, es decir, se pueden modificar
# Los sets no permiten elementos duplicados
# Los sets no permiten elementos mutables
# Los sets no permiten indexación
# Los sets no permiten slicing
# Los sets no permiten concatenación
# Los sets no permiten repetición

primer = {1, 1, 2, 3, 4, 4, 5}
segundo = {4, 5, 6, 8, 9}
segundo = set(segundo)

print(primer & segundo)  # Intersección
print(primer | segundo)  # Unión
print(primer - segundo)  # Diferencia
print(primer ^ segundo)  # Diferencia simétrica
# print(segundo)
# primer.add(6)
# primer.remove(1)
# print(primer)
