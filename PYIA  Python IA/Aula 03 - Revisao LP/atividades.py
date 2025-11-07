# Atividade 01.
# Peça a idade do usuário com base na idade fornecida, o programa deve classificar a pessoa em uma das seguintes categorias: Se a idade for menor que 12 anos, imprimir "Criança". Se a idade estiver entre 12 e 17 anos (inclusive), imprimir "Adolescente". Se a idade estiver entre 18 e 59 anos (inclusive), imprimir "Adulto". Se a idade for igual ou superior a 60 anos, imprimir "Idoso".

idade = int(input('Digite sua idade: '))

if idade < 12:
    print('Você é criança!')

elif idade <= 17:
    print('Você é adolescente!')

elif idade <= 59:
    print('Você é adulto!')
else:
    print('Você é idoso! ')

# Atividade 02.
# Faça um programa que leia 3 números e informe o maior número e o menor.

numeros = []

for i in range(3):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f'''O maior número é {maior}
O menor número é {menor}''')

# Atividade 03.
# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = []
impares = []

for i in range(10):
    numero = int(input('Digite um número: '))

    if numero %2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'''Pares: {len(pares)}
Ímpares: {len(impares)}''')

# Atividade 04.
# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

idades = 0

pessoas = int(input('Insira quantas pessoas tem na turma: '))

for i in range(pessoas):
    idade = int(input('Insira a idade: '))
    idades += idade

media = idades / pessoas

if media <=25:
    print('A turma é jovem!')

elif media <=60:
    print('A turma é adulta!')

else:
    print('A turma é idosa!')

# Atividade 05.
# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numeros = []

quantidade = int(input('Insira a quantidade de números: '))

for i in range(quantidade):
    numero = int(input('Insira o número: '))
    numeros.append(numero)

print(f'''O maior valor é {max(numeros)}
O menor valor é {min(numeros)}
A soma de todos os valores é {sum(numeros)}''')

