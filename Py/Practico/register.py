
def register_students(amount):
    students = []  # Lista para almacenar los estudiantes

    for i in range(amount):
        print(f"\n--- Registro del estudiante {i+1} ---")
        code = input("Ingrese el código del estudiante: ")
        name = input("Ingrese el nombre del estudiante: ")
        n1 = float(input("Ingrese la nota 1: "))
        n2 = float(input("Ingrese la nota 2: "))
        promedio = (n1 + n2) / 2

        # Crear un diccionario con la información del estudiante
        student = {
            "Código": code,
            "Nombre": name,
            "Nota 1": n1,
            "Nota 2": n2,
            "Promedio": promedio
        }

        # Agregar el diccionario a la lista de estudiantes
        students.append(student)

    return students


def show_student(students):
    print("\n--- Lista de Estudiantes Registrados ---")
    for student in students:
        print(f"\nCódigo: {student['Código']}")
        print(f"Nombre: {student['Nombre']}")
        print(f"Nota 1: {student['Nota 1']}")
        print(f"Nota 2: {student['Nota 2']}")
        print(f"Promedio: {student['Promedio']:.2f}")


def calculateNotes(n1, n2):
    return (n1 + n2) / 2


amount = int(input("Ingrese la cantidad de alumnos a registrar: "))
students = register_students(amount)
show_student(students)
