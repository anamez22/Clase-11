class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("El motor ha sido prendido.")

class Coche:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        self.motor = Motor(tipo_motor)

    def encender_motor(self):
        self.motor.encender()

    def estado_motor(self):
        if self.motor.encendido:
            print("El motor está prendido.")
        
coche = Coche("audi", "A5")

coche.encender_motor()
coche.estado_motor()

coche.estado_motor()           