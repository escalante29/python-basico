# ejemplo de clases
import math

class MiPunto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Objecto punto {self.x}, {self.y}'

    def distancia(self, otro_punto=None):
        if otro_punto is None:
            return math.sqrt(self.x ** 2 + self.y ** 2)
        if isinstance(otro_punto, MiPunto):
            return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)

class MiLinea(MiPunto):
    def __init__(self, par1, par2):
        p1 = super(MiLinea, self).__init__(*par1)  # TODO: Research/fix this
        p2 = super(MiLinea, self).__init__(*par1)

p1 = MiPunto(1, 3)
p2 = MiPunto(2, 4)
print(p1.distancia(p2))
#print(p1)