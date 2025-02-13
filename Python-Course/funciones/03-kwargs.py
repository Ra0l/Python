import json


def get_product(**datos):
    print(datos["id"], datos["nombre"], datos["precio"])
    print(json.dumps(datos, indent=4))


get_product(id="OO1", nombre="Laptop", precio=1000,
            stock=10, descripcion="Laptop HP")
