# Atividade 1.

# Crie uma hierarquia de classes representando formas geométricas.
# Comece com uma classe base chamada "Forma" e, em seguida, crie classes derivadas
# como "Círculo" e "Retângulo" que herdem da classe base.
# Adicione métodos para calcular área e perímetro em cada classe derivada.

import math

class Forma:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        area = self.base * self.altura
        return area


class Circulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        area = (self.base / 2)**2 * 3.14
        return area


retangulo = Retangulo(5, 10)
circulo = Circulo(5, 10)

print(retangulo)
print(circulo)
