class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase:
    def __init__(self, nombre_clase):
        self.nombre = nombre_clase
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)
            
estudiante1 = Estudiante("Ana Holguin")
estudiante2 = Estudiante("María Rivera")
estudiante3 = Estudiante("samuel Llano")

mi_clase = Clase("Quimica")


mi_clase.agregar_estudiante(estudiante1)
mi_clase.agregar_estudiante(estudiante2)
mi_clase.agregar_estudiante(estudiante3)


print("Estudiantes de la clase", mi_clase.nombre)
mi_clase.listar_estudiantes()            