# Crie uma hierarquia de classes representando formas geométricas. Comece com uma classe base chamada "Forma" e, em seguida, crie classes derivadas como "Círculo" e "Retângulo" que herdem da classe base. Adicione métodos para calcular área e perímetro em cada classe derivada.

import math

class Forma:
    def area(self):
        pass
    
    def perimetro(self):
        pass


class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raio

retangulo = Retangulo(5, 10)
circulo = Circulo(5)

print(f'''Retângulo.
Área: {retangulo.area()}
Perimetro: {retangulo.perimetro()}

Círculo.
Área: {circulo.area():.2f}
Perimetro: {circulo.perimetro():.2f}''')
