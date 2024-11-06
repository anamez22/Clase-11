
class Animal:
  def __init__(self,nombre):
    self.nombre=nombre

  def hacer_sonido(self):
    print(f"El {self.nombre} esta haciendo un sonido")

class Perro(Animal):
  def hacer_sonido(self):
    print(f"El perro {self.nombre} esta ladrando")

class Gato(Animal):
  def hacer_sonido(self):
      print(f"El gato {self.nombre} esta maullando")

el_perro= Perro("mateo")
el_gato= Gato("zeus")

el_perro.hacer_sonido()
el_gato.hacer_sonido()

