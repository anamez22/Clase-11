class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print(f"Libros escritos por {self.nombre}:")
        for libro in self.libros:
            print(f"- {libro.titulo}")

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


autor1 = Autor(" miguel de cervantes")
autor2 = Autor("william shakespeare")

libro1 = Libro("El quijote", autor1)
libro2 = Libro("La galatea", autor1)
libro3 = Libro("romeo y julieta", autor2)


autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor2.agregar_libro(libro3)


autor1.mostrar_libros()
autor2.mostrar_libros()