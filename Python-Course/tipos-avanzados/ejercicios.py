from pprint import pprint

string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]  # List Comprehension


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]

    return respuesta


def crea_mensaje(diccionario):
    mensaje = "Los que mas se reoiten son:\n"
    for key, value in diccionario.items():
        mensaje += f"El caracter {key} se repite {value} veces\n"
    return mensaje


sin_espacios = quita_espacios(string)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)
