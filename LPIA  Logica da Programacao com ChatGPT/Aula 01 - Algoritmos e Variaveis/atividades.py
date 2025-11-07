# Atividade 01.
# Crie uma variavel chamada “saudacao” , em seguida coloque uma atribuição e dentro de dado armazenado escreva “Hello World”

saudacao = 'Hello World'

# Atividade 02.
# Crie um programa que peça ao usuário para digitar:
# 1.Seu nome; 2.Sua idade; 3.Sua altura; 4.Em seguida, imprima esses valores e seus respectivos tipos.

nome = str(input('Insira seu nome: '))
idade = int(input('Insira sua idade: '))
altura = float(input('Insira sua altura: '))

print(f'Nome: {nome} | Idade: {idade} | Altura: {altura}')

# Atividade 03.
# Criar um Programa que Peça as 4 Notas Bimestrais e Mostre a Média

nota1 = float(input('Insira sua nota: '))
nota2 = float(input('Insira sua nota: '))
nota3 = float(input('Insira sua nota: '))
nota4 = float(input('Insira sua nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Sua média é {media}')

# Atividade 04.
# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês, calcule o salário total e exiba o resultado (Considere que você trabalha 20 dias no mês).

salario = float(input('Insira seu salário: '))
horas_semanais = int(input('Insira quantas horas semanais você trabalha: '))
horas_mes = horas_semanais * 4
salario_hora = salario / horas_mes

print(f'Seu salário por hora é R${salario_hora:.2f}')

# Atividade 05.
# Peça ao usuário para digitar seu nome, idade e cidade natal. Use uma f-string para formatar e exibir uma mensagem com essas informações.

nome = str(input('Insira seu nome: '))
idade = int(input('Insira sua idade: '))
cidade = str(input('Insira sua cidade natal: '))

print(f'Seu nome é {nome}, sua idade é {idade} e sua cidade natal é {cidade}')
