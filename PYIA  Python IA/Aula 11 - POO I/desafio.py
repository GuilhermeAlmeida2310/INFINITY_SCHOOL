# Crie uma classe Hotel que permita gerenciar funcionários, reservas e quartos de hotel. Os funcionários devem ter informações como nome, função e salário. O hotel deve ser capaz de receber reservas, atribuí-las a quartos e calcular a conta final.

funcionarios = {}
hospedes = {}

quartos_diponiveis = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220,
                      230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]
quartos_indisponiveis = []

class Hotel:
    def funcionarios(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def reserva(self, hospede, quarto):
        self.hospede = hospede
        self.quarto = quarto

    def ver_quartos(self, mostrar_quartos):
        self.mostrar_quartos = mostrar_quartos


hotel = Hotel()


def menu():

    while True:
        print('Gerenciamento de Hotel')
        print('1-) Gerenciar Funcionáio')
        print('2-) Fazer Reserva')
        print('3-) Ver Quartos do Hotel')
        print('4-) Sair do Gerenciador')

        opcao = int(input('Selecione o que deseja fazer: '))

        if opcao == 1:
            adicionar_funcionario = int(input('''Você quer adicionar um funcionário ao banco?
1-) Sim | 2-) Não.
Resposta: '''))
            if adicionar_funcionario == 1:
                hotel.nome = str(input('Insira o nome do funcionário: '))
                hotel.funcao = str(input('Insira a função do funcionário: '))
                hotel.salario = float(input('Insira o salário do funcionário: '))
                funcionarios['Funcionário'] = hotel.nome
                funcionarios['Função'] = hotel.funcao
                funcionarios['Salário'] = f'R${hotel.salario:.2f}'
                print(funcionarios)
                print(' ')
            elif adicionar_funcionario == 2:
                print('Saindo...')
                break
            else:
                print('Insira uma opção válida!')
                continue

        elif opcao == 2:
            adicionar_hospede = int(input('''Você quer se hospedar?
1-) Sim | 2-) Não
Resposta: '''))
            if adicionar_hospede == 1:
                hotel.hospede = str(input('Insira seu nome: '))
                print(quartos_diponiveis)
                hotel.quarto = int(input('Insira o número do quarto que quiser: '))
                hospedes[hotel.hospede] = hotel.quarto
                if hotel.quarto not in quartos_diponiveis:
                    print('Esse quarto já está ocupado ou não existe!')
                    continue
                else:
                    quartos_diponiveis.remove(hotel.quarto)
                    quartos_indisponiveis.append(hotel.quarto)
                    print(
                        f'O quarto {hotel.quarto} foi reservado por {hotel.hospede}')

        elif opcao == 3:
            ver_quartos = int(input('''Ver quartos?
1-) Sim | 2-) Não
Resposta: '''))
            if ver_quartos == 1:
                print(f'Quartos Disponíveis | {quartos_diponiveis}')
                print(f'Quartos Indisponíveis | {quartos_indisponiveis}')

            elif ver_quartos == 2:
                print('Saindo...')
                break

            else:
                print('Insira uma opção válida!')
                continue

        elif opcao == 4:
            print('Saindo...')
            break
        
        else:
            print('Insira um número válido!')
            continue


menu()
