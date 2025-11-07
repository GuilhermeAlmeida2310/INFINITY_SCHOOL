# Atividade 9.
# Desenvolva um programa que peça a idade do usuário e informe se ele é criança, adolescente, adulto ou idoso.

idade = int(input('Digite sua idade: '))

for cont in range():
    if idade > 120:
        validacao = int(input('Digite uma idade válida por favor!'))
if idade <= 11:
    print('Você é criança!')
elif idade <= 17:
    print('Você é adolescente!')
elif idade <= 59:
    print('Você é um adulto!')
elif idade < 120:
    print('Você é idoso!')

# Atividade 10.
# Crie um programa que solicite uma nota de 0 a 100 e informe o conceito (A, B, C, D, F) com base na nota.

nota = int(input('Insira sua nota: '))

if nota < 0 or nota > 100:
    print('Digite uma nota válida entre 0 e 100.')
elif nota > 75:
    print('Você tirou um A!')
elif nota > 50 and nota < 75:
    print('Você tirou um B!')
elif nota > 25 and nota < 50:
    print('Você tirou um C!')
elif nota > 0 and nota < 25:
    print('Você tirou um D!')
else:
    print('Você tirou um F!')

# Atividade 11.
# Escreva um programa que peça o dia e o mês de nascimento do usuário e informe o signo correspondente.

dia = int(input('Insira o dia do seu nascimento: '))
mes = int(input('Insira o mês do seu nascimento: '))

if (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
    print('Seu signo é de Aquário.')
elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
    print('Seu signo é de Peixes.')
elif (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
    print('Seu signo é de Áries.')
elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
    print('Seu signo é de Touro.')
elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
    print('Seu signo é de Gêmeos.')
elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
    print('Seu signo é de Câncer.')
elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
    print('Seu signo é de Leão.')
elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
    print('Seu signo é de Virgem.')
elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
    print('Seu signo é de Libra.')
elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
    print('Seu signo é de Escorpião.')
elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
    print('Seu signo é de Sagitário.')
elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
    print('Seu signo é de Sagitário.')
else:
    print('Insira uma opção válida!')

# Atividade 12.
# Desenvolva um programa que simule um sistema de login. O programa deve pedir o nome de usuário e a senha e verificar se correspondem a um usuário pré-cadastrado. Exiba mensagens apropriadas para login bem-sucedido ou falha.

nome_usuario = "Pythonn"
senha = 1991

confirmacao_nome = str(input('Confirme seu nome de usuário: '))
confirmacao_senha = int(input('Confirme sua senha: '))
print('--------------------------------------')

if confirmacao_nome == nome_usuario and confirmacao_senha == senha:
    print(f'''Seus dados estão corretos!
Bem-vindo de volta {nome_usuario}''')
else:
    print('''Nome de usuário ou senha incorretos!
Insira os dados corretos!''')

# Atividade 13.
# Desenvolva um programa que use um laço while para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

inicio = 11
while inicio > 0:
    inicio -= 1
    print(inicio)
print('Feliz Ano Novo!')

# Atividade 14.
# Desenvolva um programa que use um laço for para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

for cont in range(10, 0, -1):
    print(cont)
print('Feliz Ano Novo!')

# Atividade 15.
# Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.

numero = 1
soma = 0

while True:
    if numero > 100:
        break
    elif numero % 2 == 0:
        soma += numero
        print(numero)
    numero += 1
print(soma)

# Atividade 16.
# Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).

numero = int(input('Insira um número para ver sua tabuada: '))

for cont in range(11):
    print(f'{numero} X {cont} = {numero * cont}')

# Atividade 17.
# Escreva um programa que solicite uma palavra ao usuário e use um laço while para verificar se a palavra é um palíndromo (lê-se da mesma forma de trás para frente).

palavra = str(
    input('Insira uma palavra para verificar se é um palíndromo: ')).lower()
palavra_inversa = ''
i = len(palavra) - 1
while i >= 0:
    palavra_inversa += palavra[i]
    i -= 1
if palavra == palavra_inversa:
    print(f'A palavra {palavra} é um palíndromo!')
else:
    print(f'A palavra {palavra} não é um palíndromo!')


# Atividade 18.
# O programa deve solicitar o nome de usuário e senha até que o usuário insira as credenciais corretas ou até que o número máximo de tentativas seja atingido. Use um laço while com uma condicional para verificar as credenciais e limitar  as tentativas.

nome_usuario = 'Python'
senha = 1991
tentativas = 3

while tentativas > 0:
    confirmacao_nome = str(input('Digite seu nome de usuário: '))
    confirmacao_senha = int(input('Digite sua senha: '))

    if confirmacao_nome == nome_usuario and confirmacao_senha == senha:
        print(f'Bem-vindo de volta {confirmacao_nome}!')
        break
    else:
        tentativas -= 1
        print('Nome de usuário ou senha incorretos!')
        print(f'Tentativas restantes: {tentativas}')
