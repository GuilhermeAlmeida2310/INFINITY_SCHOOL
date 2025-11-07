# Atividade 1.
# Crie um classe chamada cachorro com os atributos: nome, raça, idade

class Cachorro:
    def __init__(self,nome,raca,idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

cachorro_ = Cachorro('Beto','Vira-Lata','9 anos')

print(f'O nome do seu cachorro é {cachorro_.nome}')
print(f'A raça do seu cachorro é {cachorro_.raca}')
print(f'A idade do seu cachorro é {cachorro_.idade}')

# Atividade 2.
# Crie um classe chamada pessoa com os atributos: nome, idade, peso, gênero.

class Pessoa:
    def __init__(self,nome,idade,peso,genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

pessoa_ = Pessoa('Guilherme',18,'76Kg','Masculino')

print(f'O nome da pessoa é {pessoa_.nome}')
print(f'Sua idade é {pessoa_.idade}')
print(f'Seu peso é {pessoa_.peso}')
print(f'Seu gênero é {pessoa_.genero}')
