import random

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)
print(
    random.random(),
    random.randint(1, 10),
    lista,
    random.choice(lista2),
    random.choices(lista2, k=3),
    random.choices("abcdcavdsbsvsdv134", k=3),
)
