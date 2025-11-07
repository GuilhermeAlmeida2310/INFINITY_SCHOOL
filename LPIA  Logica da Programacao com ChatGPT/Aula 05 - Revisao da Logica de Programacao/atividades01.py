# Atividade 1.
# Crie um programa que converta metros para centímetros. Peça ao usuário para digitar um valor em metros, armazene em uma variável e converta para centímetros.

metros = float(input('Digite um valor em metros para vê-lo em centímetros: '))
centimetros = metros * 100

print(f'{centimetros}cm')

# Atividade 2.
# Crie um programa que calcule a área de um retângulo. Peça ao usuário para digitar a largura e a altura, armazene em variáveis e calcule a área.

largura = float(input('Digite a largura do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

area = largura * altura

print(f'A área do retângulo é igual a {area}')

# Atividade 3.
# Crie um programa que calcule o Índice de Massa Corporal (IMC). Peça ao usuário para digitar seu peso e altura, armazene em variáveis e calcule o IMC.

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)
print(imc)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25.0:
    print('Peso normal')
elif imc < 30.0:
    print('Sobrepeso')
elif imc < 40.0:
    print('Obesidade')
else:
    print('Obesidade grave')

# Atividade 4.
# Crie um programa que calcule o valor futuro de um investimento usando a fórmula de juros simples. Peça ao usuário para digitar o capital inicial, a taxa de juros e o tempo de aplicação.

capital_inicial = float(input('Digite o valor do inicial do investimento: '))
taxa = float(input('Digite o valor dos juros: '))
meses = int(input('Por quantos meses o dinheiro vai ser investidos: '))

for cont in range(meses):
    futuro = capital_inicial * taxa * meses
print(f'R${futuro:.3f}')

# Atividade 5.

# Crie um algoritmo que peça quatro notas de um aluno, calcule a média e exiba se o aluno foi aprovado ou reprovado (média >= 6).

soma = 0

for cont in range(4):
    nota = float(input('Digite sua nota: '))
    soma += nota

media = soma / 4
print(media)

if media >= 6:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')

# Atividade 6.
# Desenvolva um algoritmo que calcule o preço de um produto após aplicar um desconto. Solicite o preço original e o percentual de desconto.

preco = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))

valor_desconto = preco * desconto
valor_final = preco - valor_desconto
print(
    f'Seu produto vai sair por R${valor_final:.2f} após a aplicação do desconto')

# Atividade 7.
# Desenvolva um algoritmo que converta uma quantidade de segundos fornecida pelo usuário em horas, minutos e segundos.

segundos = int(input('Digite quantos segundos você quer converter em horas: '))

horas = segundos // 3600
resto = segundos % 3600

minutos = resto // 60
segundos_restantes = resto % 60

print(f'{horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s)')

# Atividade 8.
# Crie um algoritmo que converta uma temperatura de Celsius para Fahrenheit. Solicite ao usuário a temperatura em Celsius e exiba o resultado em Fahrenheit.

temp_cels = float(
    input('Coloque aqui a temperatura em celsius para vê-la em Fahrenheit: '))

temp_fah = temp_cels * 9 / 5 + 32
print(f'A temperatura convertida para Fahrenheit é {temp_fah}ºF')
