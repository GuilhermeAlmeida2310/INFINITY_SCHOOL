# Atividade 01.
# Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele: "maçã", "banana", "uva", "laranja" e "morango". Em seguida, imprima o conjunto.

frutas = set()
frutas.add('Maçã')
frutas.add('Banana')
frutas.add('Uva')
frutas.add('Laranja')
frutas.add('Morango')

print(frutas)

# Atividade 02.
# Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.

frutas = set()
frutas.add('Maçã')
frutas.add('Banana')
frutas.add('Uva')
frutas.add('Laranja')
frutas.add('Morango')

if "Banana" in frutas:
    print('Sim')
else:
    print('Não')

# Atividade 03.
# Crie um conjunto chamado frutas_vermelhas e adicione as seguintes frutas a ele: "morango", "cereja" e "framboesa". Em seguida, imprima o conjunto.

frutas_vermelhas = set()
frutas_vermelhas.add('Morango')
frutas_vermelhas.add('Cereja')
frutas_vermelhas.add('Framboesa')

print(frutas_vermelhas)

# Atividade 04.
# Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.

frutas_vermelhas = set()
frutas_vermelhas.add('Morango')
frutas_vermelhas.add('Cereja')
frutas_vermelhas.add('Framboesa')
print(frutas_vermelhas)

frutas_vermelhas.remove('Cereja')
print(frutas_vermelhas)

# Atividade 05.
# Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.

a = {1,2,3}
b = {4,5,6}

uniao = a.union(b)

print(uniao)

# Atividades 06.
# Crie um programa que recebe dois conjuntos e exibe a interseção deles.

a = {1,2,3,4,5}
b = {3,4,5,6,7}

intersecao = a.intersection(b)

print(intersecao)

# Atividade 07.
# Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.

a = [1,2,3,4,5]
b = [3,4,5,6,7]

conj_a = set(a)
conj_b = set(b)

uniao = conj_a.union(conj_b)

print(uniao)

# Atividade 08.
# Escreva um programa que EXIBA um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações.

pessoa = {'Nome':'Guilherme',
          'Idade':18}
print(pessoa)

# Atividade 09.
# Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

dados = {'Nome':'Guilherme',
         'Idade':18,
         'Cidade':'São Paulo'}

for i in dados.items():
    print(i)

# Atividade 10.
# Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o valor ao dicionário, atualizando o valor se a chave já existir.

dados = {}

while True:
    print('Insira 0 em idade se não quiser adicionar mais nomes!')
    nome = str(input('Insira seu nome: '))
    idade = int(input('Insira sua idade: '))
    if idade < 0:
        break
    else:
        dados[nome] = idade
    

print(dados)

# Atividade 11.
# Escreva um programa que recebe um dicionário e uma lista de chaves como entrada e verifica se todas as chaves da lista existem no dicionário. A função deve retornar True se todas as chaves existirem e False caso contrário.

dicio = {1:'um',2:'dois',3:'três'}
lista = [1,2,3]

for i in lista:
    if i in dicio:
        print(True)
    else:
        print(False)

# Atividade 12.
# Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção. Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.

votos = {'Candidato_A': 0, 'Candidato_B': 0}

while True:
    print('''Escolha seu voto!
Candidato_A: 1
Candidato_B: 2
Insira 0 para encerrar a votação.''')

    voto = int(input('Insira seu voto: '))

    if voto == 1:
        votos['Candidato_A'] += 1
    elif voto == 2:
        votos['Candidato_B'] += 1
    elif voto == 0:
        print('Votação encerrada!')
        break
    else:
        print('Insira uma opção válida!')
        continue

print(f'O vencedor da eleição é {max(votos, key=votos.get)}')

# Atividade 13.
# Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.

alunos = {}

quantidade = int(input('Insira a quantidade de alunos: '))
notas = 0

for i in range(quantidade):
    nome = str(input('Insira o nome do aluno: '))
    matematica = float(input('Insira a nota de matemática: '))
    notas += matematica
    alunos[nome] = matematica

media = notas / quantidade
print(f'A média de notas da turma é {media}')
print(alunos)

# Atividade 14.
# Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em seguida, exiba a lista original e a lista sem duplicatas.

com_duplicatas = [1,2,3,4,1,2,3,5,6,7,4,5,6,8,9,10]
sem_duplicatas = set(com_duplicatas)

print(f'''Lista com Duplicatas: {com_duplicatas}
Lista sem Duplicatas: {sem_duplicatas}''')

# Atividade 15.
# Crie um programa que realize a união de múltiplos conjuntos e exiba o conjunto resultante.

a = {1,2,3,4,5}
b = {6,7,8,9,10}
c = {11,12,13,14,15}

uniao = a.union(b,c)

print(uniao)
