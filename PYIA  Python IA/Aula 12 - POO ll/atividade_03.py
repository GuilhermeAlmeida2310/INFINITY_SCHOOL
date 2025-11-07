# Crie uma classe chamada "Calculadora" com um método "somar" que pode somar dois números inteiros ou duas strings. Use o polimorfismo para implementar a sobrecarga do método "somar" para que ele funcione com diferentes tipos de entrada (números inteiros e strings). Crie exemplos de uso para demonstrar como a mesma função pode se comportar de maneira diferente com base nos tipos de entrada.

class Calculadora:
    
    def __init__(self,dado1,dado2):
        self.dado1 = dado1
        self.dado2 = dado2

    def somar(self,dado1,dado2):
        self.dado1 = dado1
        self.dado2 = dado2
        return dado1 + dado2
    
class Inteiros(Calculadora):

    def somar(self,dado1,dado2):
        self.dado1 = dado1
        self.dado2 = dado2
        return self.dado1 + self.dado2
    
class Strings(Calculadora):
    
    def somar(self,dado1,dado2):
        self.dado1 = dado1
        self.dado2 = dado2
        return self.dado1 + self.dado2

inteiros = Inteiros(10,10)
strings = Strings('Olá,','Mundo')

print(f'Números: {inteiros.dado1} + {inteiros.dado2} = {inteiros.somar(10,10)}')
print(f'Textos: {strings.dado1} + {strings.dado2} = {strings.somar('Olá, ','Mundo')}')