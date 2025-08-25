# Crie um programa que cadastre 5 alunos (nome e nota) em uma lista de tuplas.
# Em seguida, exiba o nome do aluno com a maior nota.

alunos = []

for i in range(5):
    nome = str(input('Digite o nome do aluno: '))
    nota = float(input('Digite a nota do aluno: '))
    alunos.append((nome, nota))

melhor_aluno = max(alunos, key=lambda aluno: aluno[1])

print(
    f'O aluno com a maior nota é {melhor_aluno[0]}, com a nota {melhor_aluno[1]}')
