import csv
import os

# escribir
# with open("Python-Course/archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([100, 1, "este es un twit"])
#     writer.writerow([100, 1, "otro tweet"])

# leer
# with open("Python-Course/archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# actualizar csv
with open("Python-Course/archivos/archivo.csv") as r, open("Python-Course/archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("Python-Course/archivos/archivo.csv")
    os.rename("Python-Course/archivos/archivo_temp.csv",
              "Python-Course/archivos/archivo.csv")
