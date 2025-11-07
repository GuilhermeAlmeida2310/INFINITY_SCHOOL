# Crie uma interface chamada "Veículo" com métodos "acelerar" e "frear." Em seguida, crie classes concretas como "Carro" e "Bicicleta" que implementem a interface "Veículo" e forneçam suas próprias implementações dos métodos "acelerar" e "frear." Demonstre como o polimorfismo pode ser usado para tratar diferentes tipos de veículos de maneira uniforme, chamando os métodos da interface.

class Veiculo:

    def __init__(self):
        pass

    def acelerar(self,rapido):
        self.rapido = rapido
        return f'O veiculo está acelerando? {rapido}'

    def frear(self,parar):
        self.parar = parar
        return f'O veiculo está parando? {parar}'

class Carro(Veiculo):

    def acelerar(self, rapido):
        return super().acelerar(rapido)
    
    def frear(self, parar):
        return super().frear(parar)
    
class Bike(Veiculo):

    def acelerar(self, rapido):
        return super().acelerar(rapido)
    
    def frear(self, parar):
        return super().frear(parar)
    
carro = Carro()
bike = Bike()

print(f'Carro: {carro.acelerar('Sim')} | {carro.frear('Não')}')
print(f'Bike: {bike.acelerar('Não')} | {bike.frear('Sim')}')