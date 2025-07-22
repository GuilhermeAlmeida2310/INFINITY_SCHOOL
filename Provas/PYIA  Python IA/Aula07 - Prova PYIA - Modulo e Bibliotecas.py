# Crie uma função chamada lancar_dados que utilizará o módulo random
# para simular o lançamento de dois dados.
# Cada dado deve gerar um número aleatório entre 1 e 6.
# A função deve somar os resultados desses dois lançamentos
# e retornar o valor total.

import random


def lancar_dados():
    numeros = [1, 2, 3, 4, 5, 6]
    dado1 = random.choice(numeros)
    dado2 = random.choice(numeros)
    resultado = dado1 + dado2
    print(f'''Os números lançados pelos dados foram {dado1} e {dado2}.
A soma dos números lançados é {resultado}''')
lancar_dados()
