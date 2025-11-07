# Atividade 1.
# Peça ao usuário duas idades e use operadores de comparação para verificar se a primeira idade é maior, menor ou igual à segunda.

idade_1 = int(input('Digite sua idade aqui: '))
idade_2 = int(input('Digite sua idade aqui: '))

print(idade_1 >= idade_2)

# Atividade 2.
# Peça ao usuário duas palavras e use operadores de comparação para verificar se elas são iguais.

palavra_1 = str(input('Digite a palavra aqui: '))
palavra_2 = str(input('Digite a palavra aqui: '))

print(palavra_1 == palavra_2)

# Atividade 3.
# Crie um programa que peça a idade do usuário e se ele possui habilitação (sim ou não). Use operadores lógicos para verificar se ele é maior de idade (>= 18) e possui habilitação.

idade = int(input('Digite sua idade aqui: '))
habilitacao = str(input('Você possui habilitação? '))

if idade >= 18 and habilitacao == 'Sim':
    print('Você pode dirigir. ')
elif idade >= 18 and habilitacao == 'Não':
    print('Você tem idade para dirigir, mas não possui habilitação. ')
else:
    print('Você não pode dirigir. ')

# Atividade 4.
# Escreva um programa que peça duas notas de um aluno. Use operadores lógicos para verificar se as duas notas são maiores ou iguais a 6.

nota_1 = int(input('Digite sua nota aqui: '))
nota_2 = int(input('Digite sua nota aqui: '))

if nota_1 >= 6 and nota_2 >= 6:
    print('Suas notas são maiores que 6. PARABÉNS!!!')
elif nota_1 >= 6 or nota_2 >= 6:
    print('Apenas uma de sua notas é maior que 6. Faça a recuperação.')
else:
    print('Nenhuma das sua notas é igual a 6. REPROVADO.')

# Atividade 5.
# Peça ao usuário para inserir o preço de um produto e, em seguida, use o operador de atribuição -= para aplicar um desconto de 5%.

preco = float(input('Digite o preço do seu produto aqui: '))
desconto = preco * 0.05
preco_com_desconto = preco - desconto

print(
    f'Seu desconto é de {desconto}, seu preço com desconto é de R${preco_com_desconto} ')

# Atividade 6.
# Solicite ao usuário um número e use o operador de atribuição *= para dobrar o valor e exibir o resultado.

numero = float(input('Digite o número aqui: '))

numero *= 2

print(numero)

# Atividade 7.
# Crie um programa que peça ao usuário uma frase e um caractere. Use o operador de associação in para verificar se o caractere está presente na frase.

frase = str(input('Digite sua frase e seu caractere: '))

resultado = '@' in (frase)

print(resultado)

# Atividade 8.
# Peça ao usuário para inserir uma frase e uma palavra. Use in para verificar se a palavra está na frase.

frase = str(input('Digite uma frase: '))

resultado = 'hoje' in (frase)

print(resultado)

# Atividade 9.
# Crie um programa que peça ao usuário um número e use a estrutura condicional if para verificar se ele é par ou ímpar.

numero = int(input('Digite um número aqui: '))

if numero % 2 != 0:
    print('Seu número é ímpar.')
else:
    print('Seu número é par')

# Atividada 10.
# Crie um programa que peça a nota de um aluno euse if para verificar se ele foi aprovado (nota >= 6).

nota = float(input('Digite sua nota: '))

if nota >= 6:
    print('Você foi aprovado.')
else:
    print('Você foi reprovado.')

# Atividade 11.
# Escreva um programa que peça um número e use if para verificar se ele é par ou ímpar e também se é positivo ou negativo.

numero = int(input('Digite o número: '))

if numero % 2 == 0 and numero > 0:
    print('O número é par e positivo.')
elif numero % 2 != 0 and numero > 0:
    print('O número é ímpar e positivo.')
elif numero % 2 == 0 and numero < 0:
    print('O número é par e negativo.')
else:
    print('O número é ímpar e negativo.')

# Atividade 12.
# Crie um programa que calcule o Índice de Massa Corporal (IMC) e use if para classificar o resultado em "Abaixo do peso", "Peso normal", "Sobrepeso" e "Obesidade".

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if 16 <= imc <= 18.5:
    print('Magreza ou Abaixo do peso.')
elif 18.5 < imc <= 25:
    print('Saudável.')
elif 25 < imc <= 30:
    print('Acima do peso.')
else:
    print('Obesidade.')

# Atividade 13.
# Desenvolva um programa que peça ao usuário um nome de usuário e uma senha e use if para verificar se são iguais a "admin" e "1234", respectivamente.

confirmacao1 = str(input('Digite seu nome de usúriao: '))
confirmacao2 = int(input('Digite sua senha: '))

if confirmacao1 == 'admin' and confirmacao2 == 1234:
    print('Acesso liberado!')
else:
    print('Usuário ou senha incorretos')

# Atividade 14.
# Crie um programa que peça ao usuário o preço original de um produto e a quantidade comprada. Use if para verificar se a quantidade é maior que 10 para aplicar um desconto de 10% sobre o total.

preco_ori = float(input('Insira o preço do produto: '))
quantidade = int(input('Insira a quantidade dos produtos: '))

if quantidade > 10:
    desconto = preco_ori * quantidade * 0.10
    print(f'Seu desconto é de R${desconto:.2f}')
