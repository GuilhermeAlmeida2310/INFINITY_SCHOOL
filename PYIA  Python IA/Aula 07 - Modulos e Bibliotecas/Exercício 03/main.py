from calculador_de_medidas import quadrado, retangulo, circulo

def menu():
    print('Calculador de Medidas')
    print('1-) Quadrado')
    print('2-) Retângulo')
    print('3-) Círculo')
    print('4-) Sair')
    
    while True:
        opcao = int(input('Digite uma opção: '))
        
        if opcao == 1:
            lado = float(input('Digite o lado do quadrado: '))
            area, perimetro = quadrado(lado)
            print(f'''Área: {area:.2f} cm²
Perímetro: {perimetro:.2f} cm''')

        elif opcao == 2:
            largura = float(input('Digite a largura do retângulo: '))
            altura = float(input('Digite a altura do retângulo: '))
            area, perimetro = retangulo(largura, altura)
            print(f'''Área: {area:.2f} cm²
Perímetro: {perimetro:.2f} cm''')
        
        elif opcao == 3:
            raio = float(input('Digite o raio do círculo: '))
            area, perimetro = circulo(raio)
            print(f'''Área: {area:.2f} cm²
Perímetro: {perimetro:.2f} cm''')
        
        elif opcao == 4:
            print('Encerrando o programa. Até logo!')
            break
        
        else:
            print('Digite uma opção válida!')

menu()