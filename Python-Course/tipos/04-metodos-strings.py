animal = ' chanchito feliz  '
print(animal.upper())  # CHANCHITO FELIZ (mayusculas)
print(animal.lower())  # chanchito feliz (minusculas)
print(animal.title())  # Chanchito Feliz (primera letra en mayuscula)
print(animal.find('feliz'))  # 10 (posicion de la palabra)
print(animal.capitalize())  # Chanchito feliz (primera letra en mayuscula)
# chanchito triste (reemplaza feliz por triste
print(animal.replace('feliz', 'triste'))
print(animal)  # chanchito feliz (no modifica la variable original)
print(animal.lstrip())  # chanchito feliz (elimina espacios a la izquierda)
print(animal.rstrip())  # chanchito feliz (elimina espacios a la derecha)
# chanchito feliz (elimina espacios a ambos lados)
print(animal.strip().capitalize())
print("nCH" in animal)  # False (busca la palabra en la variable)
print("nCH" not in animal)  # True (busca la palabra en la variable)
