# DESAFIO!!!
# Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair. Ela deve funcionar infinitamente, até que o usuário decida sair da calculadora. Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os calculos.

def soma(num1,num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def multiplicacao(num1,num2):
    return num1 * num2

def divisao(num1,num2):
    return num1 / num2

def menu_opcoes():
    print('Menu de Opções.')
    print('1-) Somar')
    print('2-) Subtrair')
    print('3-) Multiplicar')
    print('4-) Dividir')
    print('5-) Sair')

while True:
    menu_opcoes()

    opcao = int(input('Insira o número da opção: '))

    if opcao == 1:
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))
        print(soma(num1,num2))
    elif opcao == 2:
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))
        print(subtracao(num1,num2))
    elif opcao == 3:
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))
        print(multiplicacao(num1,num2))
    elif opcao == 4:
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))
        if num2 == 0:
            print('Insira um número diferente de 0!')
            continue
        else:
            print(divisao(num1,num2))

    elif opcao == 5:
        print('Encerrando Calculadora. Até mais!')
        break
    else:
        print('Insira uma opção válida!')
        continue