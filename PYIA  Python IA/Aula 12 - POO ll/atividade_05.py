# Crie uma classe base chamada "Animal" com um método "emitirSom." Em seguida, crie classes derivadas como "Cachorro", "Gato" e "Pássaro" que herdem de "Animal" e sobrescrevam o método "emitirSom" para cada tipo de animal. Crie uma lista de animais e percorra-a, chamando o método "emitirSom" para cada animal. Demonstre como o polimorfismo permite que diferentes tipos de animais emitam seus sons de maneira uniforme.

class Animal:

    def emitirSom(self):
        pass

class Cachorro(Animal):

    def emitirSom(self,latido):
        self.latido = latido
        return latido
        
class Gato(Animal):

    def emitirSom(self,miado):
        self.miado = miado
        return miado
    
class Passaro(Animal):

    def emitirSom(self,piado):
        self.piado = piado
        return piado
    
cachorro = Cachorro()
gato = Gato()
passaro = Passaro()

animais = [cachorro,gato,passaro]

print(f'O Cachorro faz: {cachorro.emitirSom('Au Au')}')
print(f'O Gato faz: {gato.emitirSom('Meow')}')
print(f'O Pássaro faz: {passaro.emitirSom('Piu Piu')}')
