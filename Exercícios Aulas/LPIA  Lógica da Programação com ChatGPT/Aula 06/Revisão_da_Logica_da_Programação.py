# Atividade 1.
# Conversão de Unidades:
# 1-) Crie um programa que converta metros para centímetros.
# 2-) Peça ao usuário para digitar um valor em metros, armazene
#     em uma variável e converta para centímetros.

# metros = float(input('Digite um valor em metros para vê-lo em centímetros: '))
# centimetros = metros * 100

# print(f'{centimetros}cm')

# Atividade 2.
# Cálculo de Área:
# 1-) Crie um programa que calcule a área de um retângulo.
# 2-) Peça ao usuário para digitar a largura e a altura,
#     armazene em variáveis e calcule a área.

# largura = float(input('Digite a largura do retângulo: '))
# altura = float(input('Digite a altura do retângulo: '))

# area = largura * altura

# print(f'A área do retângulo é igual a {area}')

# Atividade 3.
# Cálculo de IMC:
# 1-) Crie um programa que calcule o Índice de Massa Corporal (IMC).
# 2-) Peça ao usuário para digitar seu peso e altura, armazene em
#     variáveis e calcule o IMC.

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))

# imc = peso / (altura * altura)
# print(imc)

# if imc < 18.5:
#     print('Abaixo do peso')
# elif imc < 25.0:
#     print('Peso normal')
# elif imc < 30.0:
#     print('Sobrepeso')
# elif imc < 40.0:
#     print('Obesidade')
# else:
#     print('Obesidade grave')

# Atividade 4.
# Cálculo de Juros Simples:
# 1-) Crie um programa que calcule o valor futuro de um investimento
#     usando a fórmula de juros simples.
# 2-) Peça ao usuário para digitar o capital inicial,
#     a taxa de juros e o tempo de aplicação.

# capital_inicial = float(input('Digite o valor do inicial do investimento: '))
# taxa = float(input('Digite o valor dos juros: '))
# meses = int(input('Por quantos meses o dinheiro vai ser investidos: '))

# for cont in range(meses):
#     futuro = capital_inicial * taxa * meses
# print(f'R${futuro:.3f}')

# Atividade 5.
# Verificando a Média do Aluno:
# 1-) Crie um algoritmo que peça quatro notas de um aluno, calcule a
# média e exiba se o aluno foi aprovado ou reprovado (média >= 6).

# soma = 0

# for cont in range(4):
#     nota = float(input('Digite sua nota: '))
#     soma += nota

# media = soma / 4
# print(media)

# if media >=6:
#     print('Você foi aprovado!')
# else:
#     print('Você foi reprovado!')

# Atividade 6.
# Algoritmo de Cálculo de Desconto:
# Desenvolva um algoritmo que calcule o preço de um produto
# após aplicar um desconto. Solicite o preço original e o percentual
# de desconto.

# preco = float(input('Digite o valor do produto: '))
# desconto = float(input('Digite o valor do desconto: '))

# valor_desconto = preco * desconto
# valor_final = preco - valor_desconto
# print(f'Seu produto vai sair por R${valor_final:.2f} após a aplicação do desconto')

# Atividade 7.
# Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.

# segundos = int(input('Digite quantos segundos você quer converter em horas: '))

# horas = segundos // 3600
# resto = segundos % 3600

# minutos = resto // 60
# segundos_restantes = resto % 60

# print(f'{horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s)')

# Atividade 8.
# Algoritmo de Conversão de Temperatura:
# 1-) Crie um algoritmo que converta uma temperatura
#     de Celsius para Fahrenheit.
# 2-) Solicite ao usuário a temperatura em Celsius
#     e exiba o resultado em Fahrenheit.

# temp_cels = float(input('Coloque aqui a temperatura em celsius para vê-la em Fahrenheit: '))

# temp_fah = temp_cels * 9 / 5 + 32
# print(f'A temperatura convertida para Fahrenheit é {temp_fah}ºF')

# Atividade 9.
# 1-) Desenvolva um programa que peça a idade do usuário e
#     informe se ele é criança, adolescente, adulto ou idoso.

# idade = int(input('Digite sua idade: '))

# for cont in range():
#     if idade > 120:
#         validacao = int(input('Digite uma idade válida por favor!'))
# if idade <= 11:
#     print('Você é criança!')
# elif idade <= 17:
#     print('Você é adolescente!')
# elif idade <= 59:
#     print('Você é um adulto!')
# elif idade < 120:
#     print('Você é idoso!')

# Atividade 10.
# 1-) Crie um programa que solicite uma nota de 0 a 100
#     e informe o conceito (A, B, C, D, F) com base na nota.

# nota = float(input('Insira sua nota para vê-la como seria nos EUA: '))

# if nota < 0 or nota > 100:
#     print('Digite uma nota válida entre 0 e 100.')
# else:
#     if nota <= 25:
#         print('Sua nota é F')
#     elif nota <= 50:
#         print('Sua nota é D')
#     elif nota <= 75:
#         print('Sua nota é C')
#     elif nota <= 90:
#         print('Sua nota é B')
#     else:
#         print('Sua nota é A')

# Atividade 11.
# 1-) Escreva um programa que peça o dia e o mês de nascimento
#     do usuário e informe o signo correspondente.

# dia = int(input('Insira o dia do seu nascimento: '))
# mes = int(input('Insira o mês do seu nascimento: '))

# Atividade 12.
# 1-) Desenvolva um programa que simule um sistema de login.
# 2-) O programa deve pedir o nome de usuário e a senha e verificar
#     se correspondem a um usuário pré-cadastrado.
# 3-) Exiba mensagens apropriadas para login bem-sucedido ou falha.

# nome_usuario = "Pythonn"
# senha = 1991

# confirmacao_nome = str(input('Confirme seu nome de usuário: '))
# confirmacao_senha = int(input('Confirme sua senha: '))
# print('--------------------------------------')

# if confirmacao_nome == nome_usuario and confirmacao_senha == senha:
#     print(f'''Seus dados estão corretos!
# Bem-vindo de volta {nome_usuario}''')
# else:
#     print('''Nome de usuário ou senha incorretos!
# Insira os dados corretos!''')

# Atividade 13.
# Desenvolva um programa que use um laço while para exibir uma
# contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

# inicio = 11
# while inicio > 0:
#     inicio -=1
#     print(inicio)
# print('Feliz Ano Novo!')

# Atividade 14.
# Desenvolva um programa que use um laço for para exibir uma
# contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

# for cont in range(10,0,-1):
#     print(cont)
# print('Feliz Ano Novo!')

# Atividade 15.
# 1-) Crie um programa que use um laço while para somar
#     todos os números pares de 1 a 100 e exiba o resultado.

# numero = 1
# soma = 0

# while True:
#     if numero > 100:
#         break
#     elif numero %2 == 0:
#         soma += numero
#         print(numero)
#     numero +=1
# print(soma)

# Atividade 16.
# Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).

# numero = int(input('Insira um número para ver sua tabuada: '))

# for cont in range(11):
#     print(f'{numero} X {cont} = {numero * cont}')

# Atividade 17.
# Escreva um programa que solicite uma palavra ao usuário e
# use um laço while para verificar se a palavra é um palíndromo
# (lê-se da mesma forma de trás para frente).

# Atividade 18.
# 1-) O programa deve solicitar o nome de usuário e senha até que o
#     usuário insira as credenciais corretas ou até que o número máximo
#     de tentativas seja atingido.
# 2-) Use um laço while com uma condicional para verificar as credenciais
#     e limitar  as tentativas.

# nome_usuario = 'Python'
# senha = 1991
# tentativas = 3

# while tentativas > 0:
#     confirmacao_nome = str(input('Digite seu nome de usuário: '))
#     confirmacao_senha = int(input('Digite sua senha: '))

#     if confirmacao_nome == nome_usuario and confirmacao_senha == senha:
#         print(f'Bem-vindo de volta {confirmacao_nome}!')
#         break
#     else:
#         tentativas -=1
#         print('Nome de usuário ou senha incorretos!')
#         print(f'Tentativas restantes: {tentativas}')
