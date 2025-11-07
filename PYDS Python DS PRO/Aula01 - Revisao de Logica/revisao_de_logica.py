# Atividade 01
# Peça a idade do usuário com base na idade fornecida, o programa deve classificar a pessoa em uma das seguintes categorias: Se a idade for menor que 12 anos, imprimir "Criança". Se a idade estiver entre 12 e 17 anos (inclusive), imprimir "Adolescente". Se a idade estiver entre 18 e 59 anos (inclusive), imprimir "Adulto". Se a idade for igual ou superior a 60 anos, imprimir "Idoso".

idade = int(input('Digite sua idade: '))

if idade < 12:
    print('Você é uma criança.')
elif idade <= 17:
    print('Você é um adolescente.')
elif idade <=59:
    print('Você é um adulto.')
else:
    print('Você é um idoso.')

# Atividade 02.
# # Faça um programa que leia 3 números e informe o maior número e o menor.

numeros = []

for i in range(3):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

print(f'O maior número é {max(numeros)} e o menor número é {min(numeros)}')

# Atividade 03.
# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

soma = 0
pares = []
impares = []

for i in range(10):
    numero = int(input('Digite um número: '))
    soma += numero
    if numero %2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Soma dos números digitados: {soma}')
print(f'Quantidade de números pares: {len(pares)}')
print(f'Quantidade de números ímpares: {len(impares)}')

# Ativiadade 04.
# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

soma = 0
quantidade = int(input('Digite o número de pessoas: '))

for pessoas in range(quantidade):
    idade = int(input('Digite a idade: '))
    soma += idade
media = soma / quantidade
if media <= 25:
    print('O grupo de pessoas é Jovem.')
elif media > 25 and media <= 60:
    print('O grupo de pessoas é Adulto.')
else:
    print('O grupo de pessoas é Idoso')

# Atividade 05.
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numeros = []

quantidade = int(input('Insira a quantidade de números: '))

for i in range(quantidade):
    numero = int(input('Insira o número: '))
    numeros.append(numero)

print(f'''Maior Valor: {max(numeros)}
Menor Valor: {min(numeros)}
Soma dos Números: {sum(numeros)}''')

