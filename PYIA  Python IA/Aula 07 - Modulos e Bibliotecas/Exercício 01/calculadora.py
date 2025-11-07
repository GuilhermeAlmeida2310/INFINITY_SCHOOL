from calculadora import soma,subtracao,multiplicacao,divisao

def menu():
    print('1-) Somar')
    print('2-) Subtrair')
    print('3-) Multiplicar')
    print('4-) Dividir')
    print('5-) Sair')

    

    while True:
        opcao = int(input('Digite uma opção: '))
        if opcao == 1:
            soma()
        elif opcao == 2:
            subtracao()
        elif opcao == 3:
            multiplicacao()
        elif opcao == 4:
            divisao()
        elif opcao == 5:
            print('Encerrando o programa. Até a próxima!')
            break
        else:
            print('Digite uma opção válida!')
            
menu()