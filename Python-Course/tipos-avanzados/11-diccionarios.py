punto = {"x": 10, "y": 20}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45

# print(punto, punto["lala"])

if "lala" in punto:
    print(punto["lala"])
else:
    print("No existe la llave lala")

# Si no existe la llave, devuelve el segundo argumento
print(punto.get("lala", "No existe la llave lala"))
print(punto.get("x"))

del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)


usuarios = [
    {id: 1, "nombre": "Juan", "apellido": "Perez"},
    {id: 2, "nombre": "Maria", "apellido": "Gomez"},
    {id: 3, "nombre": "Pedro", "apellido": "Garcia"}
]


for usuario in usuarios:
    print(usuario["nombre"], usuario["apellido"])
