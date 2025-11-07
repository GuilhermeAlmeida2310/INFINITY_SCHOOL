# DESAFIO!!!
# Suponha que você está gerenciando uma competição esportiva e tem uma lista de tuplas representando os resultados das equipes em diferentes modalidades. Cada tupla contém o nome da equipe, seguido por uma lista de pontuações obtidas em cada rodada da competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses valores em uma nova lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a classificação final das equipes, mostrando o nome da equipe e sua média, da equipe com a pontuação mais alta para a mais baixa.

equipes = [('Time 1', [3, 1, 0]), ('Time 2', [3, 3, 0]), ('Time 3', [3, 1, 1])]
medias = []
classificacao = []
for cont in range(len(equipes)):
    medias.append(sum(equipes[cont][1]) / 3)
    classificacao.append((medias[cont], equipes[cont][0]))
classificacao.sort()
classificacao.reverse()
print(f'''Classificação Geral.
1ºLugar {classificacao[0][1]}| Média: {classificacao[0][0]:.2f}
2ºLugar {classificacao[1][1]}| Média: {classificacao[1][0]:.2f}
3ºLugar {classificacao[2][1]}| Média: {classificacao[2][0]:.2f}''')
