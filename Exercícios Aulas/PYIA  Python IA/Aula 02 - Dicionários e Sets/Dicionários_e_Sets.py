# Atividade 1.
# Crie um conjunto vazio chamado frutas e adicione as
# seguintes frutas a ele:"maçã","banana","uva","laranja"
# e"morango". Em seguida, imprima o conjunto.

# frutas = set()

# frutas.add('Maçã')
# frutas.add('Banana')
# frutas.add('Uva')
# frutas.add('Laranja')
# frutas.add('Morango')
# print(frutas)

# Atividade 2.
# Verifique se a fruta "banana" está presente no
# conjunto frutas e imprima o resultado.

# frutas = set()

# frutas.add('Maçã')
# frutas.add('Banana')
# frutas.add('Uva')
# frutas.add('Laranja')
# frutas.add('Morango')
# print('Banana' in frutas)

# Atividade 3.
# 1-) Crie um conjunto chamado frutas_vermelhas e adicione
#     as seguintes frutas a ele:"morango","cereja"e"framboesa".
# 2-) Em seguida, imprima o conjunto.

# frutas_vermelhas = set()

# frutas_vermelhas.add('Morango')
# frutas_vermelhas.add('Cereja')
# frutas_vermelhas.add('Framboesa')
# print(frutas_vermelhas)

# Atividade 4.
# 1-) Remova a fruta "cereja" do conjunto frutas_vermelhas e
# 2-) Imprima o conjunto atualizado.

# frutas_vermelhas = set()

# frutas_vermelhas.add('Morango')
# frutas_vermelhas.add('Cereja')
# frutas_vermelhas.add('Framboesa')
# print(frutas_vermelhas)

# frutas_vermelhas.remove('Cereja')
# print(frutas_vermelhas)

# Atividade 5.
# 1-Crie dois conjuntos, A e B, e realize a união dos dois
# conjuntos.

# a = set([1,2,3])
# b = set([4,5,6])

# resultado = a.union(b)
# print(resultado)

# Atividade 6.
# Crie um programa que recebe dois conjuntos e
# exibe a interseção deles.

# lista_de_convidados1 = {'Juan','Gustavo','Guilherme','Renan'}
# lista_de_convidados2 = {'Henrique', 'Renan', 'Juan', 'Gustavo'}

# print(lista_de_convidados1.intersection(lista_de_convidados2))

# Atividade 7.
# Escreva um programa que receba duas listas e calcule a união
# dos elementos únicos dessas listas, usando conjuntos.

# lista1 = [1,2,3,4]
# lista2 = [3,4,5,6]

# conjunto1 = set(lista1)
# conjunto2 = set(lista2)

# resultado = (conjunto1.union(conjunto2))
# print(resultado)

# Atividade 8.
# Escreva um programa que EXIBA um dicionário contendo informações
# de pessoas (nome, idade) e exiba essas informações.

# nomes_idades = {'Maria':17,
#          'Guilherme':18,
#          'Beto': 10}

# for nome, idade in nomes_idades.items():
#     print(f'''Nome: {nome}
# Idade: {idade}''')
