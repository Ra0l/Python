# def es_palindromo(texto):
#     # Elimina los espacios y convierte a minúsculas
#     texto = texto.replace(' ', '').lower()
#     return texto == texto[::-1]  # Compara el texto con su inverso


# print(es_palindromo('Anita lava la tina'))  # True

def no_space(texto):
    nuevo_texto = ""
    for char in texto:  # Recorre cada caracter del texto
        if char != " ":  # Si el caracter no es un espacio
            nuevo_texto += char  # Agrega el caracter al nuevo texto
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        # Agrega el caracter al principio del texto_al_reves
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("Amo la Paloma"))
print(es_palindromo("Hola mundo"))
