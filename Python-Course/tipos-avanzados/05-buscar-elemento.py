mascotas = ["Wolf", "Luna", "Wolf", "Toby", "Bella"]

# Buscar el índice de un elemento en la lista
print(mascotas.index("Toby"))  # 2
print(mascotas.index("Bella"))  # 3
print(mascotas.index("Wolf"))  # 0
print(mascotas.index("Luna"))  # 1
# print(mascotas.index("Firulais"))  # ValueError: 'Firulais' is not in list

print("Quantity: ", mascotas.count("Wolf"))  # 1
if "Wolf" in mascotas:
    print("Wolf está en la lista")
