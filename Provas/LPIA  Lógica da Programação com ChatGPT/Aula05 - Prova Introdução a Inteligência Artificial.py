# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. 
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, 
# pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.
# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou 
# reprovado, considerando que a média mínima para aprovação é 7.0. 
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.
# Ao final, exiba a média geral da turma.

soma_media = 0
numero_de_alunos = int(input('Digite o número de alunos aqui: '))
for cont in range(numero_de_alunos):
    soma = 0
    alunos_nome = str(input('Escreva o nome do aluno aqui: '))
    for cont in range(3):
        notas = float(input('Digite a nota aqui: '))
        soma += notas
    media = soma / 3
    soma_media += media
    print('-'*20)
    print(f'Aluno: {alunos_nome}')
    print(f'Média: {media:.2f}') 
    if media >= 7:
        print('Parabéns, você foi aprovado!')
    else:
        print('Você foi reprovado!')
    print('-'*20)
media_turma = soma_media / numero_de_alunos
print('A média da turma é igual a ', media_turma )