# Crie uma hierarquia de classes que represente veículos. Comece com uma classe base "Veículo" e, em seguida, crie classes derivadas como "Carro" e "Bicicleta." Adicione métodos para definir atributos, como "cor" e "modelo, "e permita a chamada de métodos em cadeia para configurar esses atributos.

class Veiculo:
    def __init__(self):
        self.cor = None
        self.modelo = None


class Carro(Veiculo):

    def cores(self,cor):
        self.cor = cor
        return f'Cor: {cor}'
        
    def modelos(self,modelo):
        self.modelo = modelo
        return f'Modelo: {modelo}'

class Bike(Veiculo):

    def cores(self,cor):
        self.cor = cor
        return f'Cor: {cor}'

    def modelos(self,modelo):
        self.modelo = modelo
        return f'Modelo: {modelo}'
        

carro = Carro()
bike = Bike()

print(f'Carro | {carro.cores('Branco')} | {carro.modelos('Gol com escada')}')
print(f'Bike | {bike.cores('Preto')} | {bike.modelos('BMX')}')