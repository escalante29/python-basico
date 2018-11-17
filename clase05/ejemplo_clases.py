#motor


class Motor:
    def __init__(self, potencia, cilindros_motor):
        self.potencia = potencia
        self.cilindros_motor = cilindros_motor

mi_motor = Motor(1500, 4)

class Llanta:
    def __init__(self, tamano, color_llanta):
        self.tamano = tamano
        self.color_llanta = color_llanta

mi_llanta = Llanta(8, 'negro')


class Asiento:
    def __init__(self, material_asiento, color_asiento):
        self.material_asiento = material_asiento
        self.color_asiento = color_asiento

mi_asiento = Asiento('cuero', 'rojo')


class Carro(mi_motor, mi_asiento, mi_llanta):
    def __init__(self, potencia, cilindros_motor, tamano, color_llanta, material_asiento, color_asiento):
        super(Carro, self).

pass
