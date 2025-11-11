# Crie uma classe Hotel que permita gerenciar funcionários, reservas e quartos de hotel. Os funcionários devem ter informações como nome, função e salário. O hotel deve ser capaz de receber reservas, atribuí-las a quartos e calcular a conta final.

funcionarios = {}
hospedes = {}

quartos_diponiveis = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220,
                      230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]
quartos_indisponiveis = []
precos = {'1 Pessoa': 100, '2 Pessoas': 150,
          '3 á 4 Pessoas': 200, '5 á 6 Pessoas': 250}


class Hotel:
    def funcionarios(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def reserva(self, hospede, qtd_hospedes, quarto, valor_quarto, ):
        self.hospede = hospede
        self.qtd_hospedes = qtd_hospedes
        self.quarto = quarto
        self.valor_quarto = valor_quarto

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
            hotel.nome = str(input('Insira o nome do funcionário: '))
            hotel.funcao = str(input('Insira a função do funcionário: '))
            hotel.salario = float(input('Insira o salário do funcionário: '))
            funcionarios['Funcionário'] = hotel.nome
            funcionarios['Função'] = hotel.funcao
            funcionarios['Salário'] = f'R${hotel.salario:.2f}'
            print(funcionarios)
            print(' ')

        elif opcao == 2:
            hotel.hospede = str(input('Insira seu nome: '))
            hotel.qtd_hospedes = int(
                input('Insira em quantas pessoas você está: '))
            if hotel.qtd_hospedes == 1:
                print(
                    f'Quartos para uma pessoa: {quartos_diponiveis[0:4]} | Preço: R${precos["1 Pessoa"]:.2f}')
            elif hotel.qtd_hospedes == 2:
                print(
                    f'Quartos para duas pessoas: {quartos_diponiveis[5:15]} | Preço: R${precos["2 Pessoas"]:.2f}')
            elif hotel.qtd_hospedes == 3 or hotel.qtd_hospedes == 4:
                print(
                    f'Quartos para três ou 4 pessoas: {quartos_diponiveis[16:26]} | Preço: R${precos["3 á 4 Pessoas"]:.2f}')
            elif hotel.qtd_hospedes == 5 or hotel.qtd_hospedes == 6:
                print(
                    f'Quartos para 5 ou 6 pessoas: {quartos_diponiveis[27:31]} | Preço: R${precos["5 á 6 Pessoas"]:.2f}')
            else:
                print('Infelizmente só temos quartos até 6 pessoas!')
                continue
            hotel.quarto = int(input('Insira o número do quarto que quiser: '))
            print(f'O quarto {hotel.quarto} foi reservado por {hotel.hospede}')
            hospedes[hotel.hospede] = hotel.quarto
            if hotel.quarto not in quartos_diponiveis:
                print('Esse quarto já está ocupado ou não existe!')
                continue
            else:
                quartos_diponiveis.remove(hotel.quarto)
                quartos_indisponiveis.append(hotel.quarto)

        elif opcao == 3:
            print(f'Quartos Disponíveis | {quartos_diponiveis}')
            print(f'Quartos Indisponíveis | {quartos_indisponiveis.sort()}')

        elif opcao == 4:
            print('Saindo...')
            break

        else:
            print('Insira um número válido!')
            continue


menu()
