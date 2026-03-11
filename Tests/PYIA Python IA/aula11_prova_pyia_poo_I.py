# Crie três classes separadas e independentes: Animal, Cachorro e Gato.
# Cada classe deve ter um método chamado falar (), que imprime uma mensagem específica na tela:
# - A classe Animal deve imprimir: "Este animal faz um som genérico."
# - A classe Cachorro deve imprimir: "O cachorro está latindo."
# - A classe Gato deve imprimir: "O gato está miando."

# Regras:
# - As classes não devem se relacionar entre si.
# - Cada classe deve ser criada de forma independente.
# - No final, crie um objeto para cada uma das classes e chame o método falar () de cada objeto.

class Animal:
    def falar(self):
        return f'O som do animal é genérico.'

animal_ = Animal()

print(animal_.falar())

class Cachorro:
    def falar(self):
        return f'O cachorro está latindo.'
    
cachorro_ = Cachorro()

print(cachorro_.falar())

class Gato:
    def falar(self):
        return f'O gato está miando.'
    
gato_ = Gato()

print(gato_.falar())
