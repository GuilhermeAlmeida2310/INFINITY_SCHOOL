# Atividade 1.
# 1-) Faça a definição de uma lista contendo os
#     números de 1 até 5.
# 2-) Finalmente, utilize o print() para exibir os
#     valores da lista.

# lista = [1,2,3,4,5]
# print(lista)

# Atividade 2.
# 1-) Faça a definição de uma lista contendo as vogais.
# 2-) Finalmente, utilize o print() para exibir os valores da lista.

# lista = ['a','e','i','o','u']
# print(lista)

# Atividade 3.
# 1-) Defina uma lista com 5 itens que tenha, pelo menos, 3
#     classes diferentes.
# 2-) Utilize o print() para exibir o terceiro elemento dessa lista.

# lista = [1,2.0,'Gato',True,3]
# print(lista[2])

# Atividade 4.
# 1-) Escreva um código que receba uma lista de números como entrada e
# 2-) Retorne a médiados números da lista.

# lista = [1,2,3,4,5]
# soma = 0
# for lista in lista:
#     soma += lista
# media = soma / 5
# print(media)

# Atividade 5.
# 1-) Escreva um código que receba uma lista como entrada e
# 2-) Retorne uma nova lista com todas as duplicatas removidas,
#     mantendo a ordem original dos elementos.

# Atividade 6.
# Escreva um código que receba uma lista como entrada e retorne
# uma nova lista com os elementos na ordem inversa.

# lista = [1,2,3,4,5]
# print(lista[::-1])

# Atividade 7.
# Escreva um código que receba uma lista de números como entrada e
# retorne uma nova lista com os números pares ordenados de forma
# crescente e os ímpares mantidos na mesma ordem original.

# lista = [1,3,4,6,7,5,8,2,10,9]
# lista_par = []

# for item in lista:
#     if item %2 == 0:
#         lista_par.append(item)
# lista_par.sort()

# nova_lista = []

# for item in lista:
#     if item %2 == 0:
#         menor_par = lista_par.pop(0)
#         nova_lista.append(menor_par)
#     else:
#         nova_lista.append(item)
# print(nova_lista)

# Atividade 8.
# Escreva um código que receba uma lista de números como entrada
# e retorne uma lista contendo a soma de cada par de elementos
# consecutivos da lista original.

# lista = [1,2,3,4,5]
# soma_lista = []

# for cont in range(len(lista)-1):
#     soma = lista[cont] + lista[cont+1]
#     soma_lista.append(soma)
# print(soma_lista)

# DESAFIO!!!
# Suponha que você está gerenciando uma competição esportiva e tem
# uma lista de tuplas representando os resultados das equipes em
# diferentes modalidades. Cada tupla contém o nome da equipe, seguido
# por uma lista de pontuações obtidas em cada rodada da competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a classificação final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a
# mais baixa.

# soma1 = 0
# soma2 = 0
# soma3 = 0
# soma4 = 0
# medias = []
# equipes = [
#     ('Equipe Preta', [3, 3, 3, 1, 0]),
#     ('Equipe Vermelha', [3, 3, 1, 1, 0]),
#     ('Equipe Azul', [3, 3, 1, 0, 0]),
#     ('Equipe Amarela', [3, 1, 1, 1, 0])
# ]

# for pontos in equipes[0][1]:
#     soma1 += pontos
#     media = soma1 / 5
# medias.append(media)
# for pontos in equipes[1][1]:
#     soma2 += pontos
#     media = soma2 / 5
# medias.append(media)
# for pontos in equipes[2][1]:
#     soma3 += pontos
#     media = soma3 / 5
# medias.append(media)
# for pontos in equipes[3][1]:
#     soma4 += pontos
#     media = soma4 / 5
# medias.append(media)

# classificacao = [(f'Equipe Preta. Média: {medias[0]}'),
#                  (f'Equipe Vermelha. Média: {medias[1]}'),
#                  (f'Equipe Azul. Média: {medias[2]}'),
#                  (f'Equipe Amarela. Média: {medias[3]}')]
# print(f'''Nome da Equipe e Média de Pontuação: {classificacao[0]}
# Nome da Equipe e Média de Pontuação: {classificacao[1]}
# Nome da Equipe e Média de Pontuação: {classificacao[2]}
# Nome da Equipe e Média de Pontuação: {classificacao[3]}''')

