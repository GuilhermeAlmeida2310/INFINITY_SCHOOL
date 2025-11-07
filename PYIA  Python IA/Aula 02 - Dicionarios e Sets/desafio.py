# Passo 01.
# Cadastro de Alunos: O programa deve permitir ao usuário cadastrar alunos. Cada aluno terá as seguintes informações: nome, idade e notas em três disciplinas: Matemática, Ciências e História. Os dados de cada aluno devem ser armazenados em um dicionário com as seguintes chaves: 'nome', 'idade', 'notas'. As notas devem ser armazenadas em uma tupla.

# Passo 02.
# Visualização de Alunos: O programa deve permitir ao usuário visualizar todos os alunos cadastrados, exibindo suas informações de forma organizada. Média de Notas: O programa deve calcular a média das notas de cada aluno e exibi-la. Aluno com Melhor Média: O programa deve identificar e exibir o aluno com a melhor média de notas.

alunos = []
qtd_alunos = int(input('Insira quantos alunos você quer cadastrar: '))

for i in range(qtd_alunos):
    nome = str(input('Digite o nome do aluno: '))
    idade = int(input('Digite a idade do aluno: '))
    nota1 = float(input('Insira sua nota de matemática: '))
    nota2 = float(input('Insira sua nota de ciências: '))
    nota3 = float(input('Insira sua nota de história: '))
    media = (nota1 + nota2 + nota3) / 3
    aluno = {
        'Nome': nome,
        'Idade': idade,
        'Notas': (nota1, nota2, nota3),
        'Média': media
    }
    alunos.append(aluno)

melhor_aluno = alunos[0]

for aluno in alunos:
    if aluno['Média'] > melhor_aluno['Média']:
        melhor_aluno = aluno

print(f'Informações Alunos: {alunos}')
print(f"Maior Média: {melhor_aluno['Nome']} ({melhor_aluno['Média']:.2f})")


