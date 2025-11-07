# Crie uma classe Calculadora que tenha métodos para realizar operações matemáticas básicas (+ , - , *, / ).

class Calculadora:
    def soma(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return num1 + num2

    def sub(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return num1 - num2

    def mult(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return num1 * num2

    def divi(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

        if num2 == 0:
            print('Não é possível fazer a divisão por 0!')
        else:
            return num1 / num2

calculadora = Calculadora()

def menu():
    while True:
        print('Calculadora')
        print('1-) Somar')
        print('2-) Subtrair')
        print('3-) Multiplicar')
        print('4-) Dividir')
        print('5-) Sair')
        print('')
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            num1 = float(input('Digite o Número: '))
            num2 = float(input('Digite o Número: '))
            resultado = calculadora.soma(num1,num2)
            print(f'Resultado: {resultado}')
            print('')

        elif opcao == 2:
            num1 = float(input('Digite o Número: '))
            num2 = float(input('Digite o Número: '))
            resultado = calculadora.sub(num1,num2)
            print(f'Resultado: {resultado}')
            print('')

        elif opcao == 3:
            num1 = float(input('Digite o Número: '))
            num2 = float(input('Digite o Número: '))
            resultado = calculadora.mult(num1,num2)
            print(f'Resultado: {resultado}')
            print('')

        elif opcao == 4:
            num1 = float(input('Digite o Número: '))
            num2 = float(input('Digite o Número: '))
            resultado = calculadora.divi(num1,num2)
            print(f'Resultado: {resultado}')
            print('')

        elif opcao == 5:
            print('Fechando a Calculadora. Até mais!')
            break

        else:
            print('Digite uma opção válida!')
            continue
menu()