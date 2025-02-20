from io import open

# escritura
# texto = "Hola mundo"

# archivo = open("Python-Course/archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# lectura
# archivo = archivo = open("Python-Course/archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista
# archivo = archivo = open("Python-Course/archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# with y seek
# with open("Python-Course/archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# agregar
# archivo = archivo = open("Python-Course/archivos/hola-mundo.txt", "a+")
# archivo.write("chao mundo")
# archivo.close()

# lectura y escritura
with open("Python-Course/archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz"
    archivo.writelines(texto)
