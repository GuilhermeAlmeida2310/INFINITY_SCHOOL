# Você está criando um programa em Python para simular um jogo simples de adivinhação.
# O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
# O jogador terá até 3 tentativas para acertar o número.

# Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas 
# tentativas até acertar ou atingir o limite de tentativas. Utilize a estrutura else para 
# exibir uma mensagem de encorajamento caso o jogador acerte e uma mensagem de consolo 
# caso as 3 tentativas se esgotem sem sucesso.

num_fix = 8 # número que o jogador deve acertar.
cont = 0 # contador para a condição de repetição.
while cont < 3:
    num_player = int(input('Adivinhe o número: '))
    if num_player == 8:
        break
    while True:
        if num_fix == num_player:
            print('Você acertou!! Parabéns pae!!')
            break
        else:
            print('Você errou! Tente novamente!')
            cont += 1
            break
if num_player == 8:
    print('Você é dos bons mesmo em meu consagrado.')
else:
    print('Você é muito horrível! MELHORE PAE')


