from pathlib import Path
from time import ctime

archivo = Path("Python-Course/archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

# print(archivo.stat())

print("acceso", ctime(archivo.stat().st_atime))  # timestamp fecha unix
print("creacion", ctime(archivo.stat().st_ctime))  # timestamp fecha unix
print("modificación", ctime(archivo.stat().st_mtime))  # timestamp fecha unix
