# Atividade 01.
# Crie um programa que será uma calculadora. Nesta calculadora você deverá ter um módulo para as operações matemáticas, o arquivo principal deverá conter apenas um menu de escolha para o usuário (soma, subtração, multiplicação e divisão).

def soma():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    print(f'{num1} + {num2} = {num1 + num2}')


def subtracao():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    print(f'{num1} - {num2} = {num1 - num2}')


def multiplicacao():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    print(f'{num1} X {num2} = {num1 * num2}')


def divisao():
    while True:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        if num1 == 0:
            print('Divisor não pode ser 0. Digite novamente.')
            continue
        elif num2 == 0:
            print('Divisor não pode ser 0. Digite novamente.')
        print(f'{num1} / {num2} = {num1 / num2}')
        break
