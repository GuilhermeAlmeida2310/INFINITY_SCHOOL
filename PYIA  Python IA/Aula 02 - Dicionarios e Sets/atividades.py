# # Atividade 01.
# # Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele:"maçã","banana","uva","laranja" e"morango". Em seguida, imprima o conjunto.

frutas = set()

frutas.add('Maçã')
frutas.add('Banana')
frutas.add('Uva')
frutas.add('Laranja')
frutas.add('Morango')
print(frutas)

# # Atividade 02.
# # Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.

frutas = set()

frutas.add('Maçã')
frutas.add('Banana')
frutas.add('Uva')
frutas.add('Laranja')
frutas.add('Morango')
print('Banana' in frutas)

# # Atividade 03.
# # Crie um conjunto chamado frutas_vermelhas e adicione as seguintes frutas a ele:"morango","cereja"e"framboesa". Em seguida, imprima o conjunto.

frutas_vermelhas = set()

frutas_vermelhas.add('Morango')
frutas_vermelhas.add('Cereja')
frutas_vermelhas.add('Framboesa')
print(frutas_vermelhas)

# # Atividade 04.
# # Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.

frutas_vermelhas = set()

frutas_vermelhas.add('Morango')
frutas_vermelhas.add('Cereja')
frutas_vermelhas.add('Framboesa')
print(frutas_vermelhas)

frutas_vermelhas.remove('Cereja')
print(frutas_vermelhas)

# # Atividade 05.
# # Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.

a = set([1,2,3])
b = set([4,5,6])

resultado = a.union(b)
print(resultado)

# # Atividade 06.
# # Crie um programa que recebe dois conjuntos e exibe a interseção deles.

lista_de_convidados1 = {'Juan','Gustavo','Guilherme','Renan'}
lista_de_convidados2 = {'Henrique', 'Renan', 'Juan', 'Guilherme'}

print(lista_de_convidados1.intersection(lista_de_convidados2))

# # Atividade 07.
# # Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.

lista1 = [1,2,3,4]
lista2 = [3,4,5,6]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

resultado = (conjunto1.union(conjunto2))
print(resultado)

# # Atividade 08.
# # Escreva um programa que EXIBA um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações.

nomes_idades = {'Maria':17,
         'Guilherme':18,
         'Beto': 10}

for nome, idade in nomes_idades.items():
    print(f'''Nome: {nome}
Idade: {idade}''')

# # Atividade 09.
# # Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

dicionario = {'Nome: ':'Guilherme','Idade: ':18,'Cidade: ':'São Paulo'}

print('Você quer ver chaves ou valores?')

ver = int(input('1-)Chaves 2-)Valores: '))
for chaves in dicionario.keys():
    if ver == 1:
        print(chaves)
for valores in dicionario.values():
    if ver == 2:
        print(valores)

# # Atividade 10.
# # Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o valor ao dicionário, atualizando o valor se a chave já existir.

pessoas = {}
quantidade = int(input('Insira quantas pessoas você quer cadastrar: '))

for pessoa in range(quantidade):
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Insira a idade da pessoa: '))
    pessoas[nome] = idade

for chave, valor in pessoas.items():
    print(f"Nome: {chave} | Idade: {valor}")

# # Atividade 11.
# # Escreva um programa que recebe um dicionário e uma lista de chaves como entrada e verifica se todas as chaves da lista existem no dicionário. A função deve retornar True se todas as chaves existirem e False caso contrário.

dicionario_nomes = {'Mariana': 22, 'Rafael': 31,
              'Clara': 19, 'Vinícius': 27, 'Tatiane': 35}

lista_nomes = ['Mariana','Rafael','Clara','Vinícius','Tatiane',]

for pessoas in lista_nomes:
    if pessoas not in dicionario_nomes:
        print('Nem todos os nomes se encontra no dicionário!')
else:
    print('Todos os nomes se encontra no dicionário!')

# # Atividade 12.
# # Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção. Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.

votos = {'Candidato_A':0, 'Candidato_B':0}

while True:
    print('''Insira 22 para Candidato_A.
Insira 13 para Candidato_B.
Insira 0 para encerrar a votação.''')
    opcao = int(input('Insira seu voto: '))

    if opcao == 22:
        votos['Candidato_A'] +=1
    elif opcao == 13:
        votos['Candidato_B'] +=1
    elif opcao == 0:
        print('Votação Encerrada!')
        break
    else:
        print('Digite uma opção válida!')
        continue
print(votos)

# # Atividade 13.
# # Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.

alunos = {'Ana Beatriz':8.5, 'Lucas Henrique':7.0, 'Mariana Souza':9.0, 'Rafael Almeida':7.0, 'João Pedro':8.0}
soma = 0

for notas in alunos.values():
    soma += notas

media = soma / len(alunos)

print(f'A média dos alunos é {media:.2f}')

# # Atividade 14.
# # Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em seguida, exiba a lista original e a lista sem duplicatas.

numeros = [1,2,3,1,4,5,6,2,3,7,8,1]

numeros_sem_copias = set(numeros.copy())

print(f'''Lista Original: {numeros}
Lista sem Duplicatas: {numeros_sem_copias}''')

# # Atividade 15.
# # Crie um programa que realize a união de múltiplos conjuntos e exiba o conjunto resultante.

set1 = set([1,2,3])
set2 = set([4,5,6])
set3 = set([7,8,9])
set4 = set([10,11,12])

uniao1 = set1.union(set2)
uniao2 = set3.union(set4)
uniao_total = uniao1.union(uniao2)

print(uniao_total)

