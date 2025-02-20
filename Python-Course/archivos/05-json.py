import json
from pathlib import Path

# escribir json
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# data = json.dumps(productos)
# Path("Python-Course/archivos/productos.json").write_text(data)

# leer json
data = Path("Python-Course/archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)

# modificar json
productos[0]["name"] = "Chanchito feliz"
Path("Python-Course/archivos/productos.json").write_text(json.dumps(productos))
