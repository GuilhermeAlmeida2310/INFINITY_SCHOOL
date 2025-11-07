# Desenvolva um jogo de adivinhação em que o programa escolhe um número aleatório e desafia o jogador a adivinhá-lo. Forneça dicas ao jogador, indicando se o número é maior ou menor do que a adivinhação atual.

import random

aleatorio = random.choice(range(101))
tentativas = 0

while True:
    print('Insira um número de 0 a 100')
    numero = int(input('Insira seu palpite: '))
    tentativas +=1

    if numero < aleatorio:
        print('Seu palpite é maior que o número sorteado! HAHAHA')
    elif numero > aleatorio:
        print('Seu palpite é menor que o número sorteado! HAHAHA')
    else:
        print('Você infelizmente acertou ;-;')
        break
print(f'Tentativas: {tentativas}')
