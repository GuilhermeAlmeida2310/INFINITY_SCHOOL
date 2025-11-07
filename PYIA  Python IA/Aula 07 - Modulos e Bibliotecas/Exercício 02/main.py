from manipulacao_strings import inverter, contar_palavras, palindromo


def menu():
    print('1-) Inverter palavra')
    print('2-) Contar palavras')
    print('3-) Verificar palíndromo')
    print('4-) Sair')

    while True:
        opcao = int(input('O que você quer fazer: '))
        if opcao == 1:
            palavra = str(input('Digite uma palavra: '))
            print(f'Palavra invertida: ', inverter(palavra))
        elif opcao == 2:
            palavra = str(input('Digite uma frase: '))
            print(f'Número de palavras: ', contar_palavras(palavra))
        elif opcao == 3:
            palavra = str(input('Digite uma palavra: '))
            if palindromo(palavra):
                print('A palavra é um palíndromo.')
            else:
                print('A palavra não é um palíndromo.')
        elif opcao == 4:
            print('Encerrando o programa. Até logo!👋')
            break
        else:
            print('Digite uma opção válida!')
            continue


menu()
