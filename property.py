class Producto:
  def __init__(self,nombre,precio):
    self._nombre=nombre
    self._precio=precio

  @property
  def nombre(self):
    return self._nombre

  @property
  def precio(self):
    return self._precio

  @precio.setter
  def validar_precio(self,nuevo):
       if nuevo >=0:
        self._precio=nuevo
       else:
         print("precio no válido")

  def Mostrar_info(self):
      print(f"Producto: {self._nombre} \nPrecio:{self._precio}")


producto=Producto("cama",1800000)
producto.Mostrar_info()

producto.validar_precio=-9