class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):  # Methodos
        print(f"{self.edad} dice: Guau!!")


mi_perro = Perro("Chanchito", 1)
mi_perro.habla()
