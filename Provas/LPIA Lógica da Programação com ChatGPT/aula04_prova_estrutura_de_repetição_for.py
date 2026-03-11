# Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive). Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

inicio = int(input('Digite o número do início: '))
fim = int(input('Digite o número do fim: '))
soma = 0
for cont in range(inicio, fim, 1):
    if cont % 2 == 0: # par
        soma += cont
    elif cont % 2 == 1: #impar
        cont += 0

if soma > 0:    
    print(f'A soma dos números pares é igual a {soma}.') 
else:
    print('Não há números pares na contagem.')