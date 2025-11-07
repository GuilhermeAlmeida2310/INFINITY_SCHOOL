# Crie uma classe Empresa que permita gerenciar funcionários. Os funcionários devem ter informações como nome, cargo e salário. A empresa deve ser capaz de adicionar, remover e listar funcionários.

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __repr__(self):
        return f'{self.nome}|{self.cargo}|R${self.salario:.2f}'


class Empresa:

    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'{funcionario.nome} foi adicionado ao Banco de Dados!')

    def remover_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            print(f'{funcionario.nome} foi removido do Banco de Dados!')
        else:
            print('O funcionário não foi emcontrado no Banco de Dados')

    def lista_funcionarios(self):
        if not self.funcionarios:
            print('A lista de funcionários está vazia!')
        else:
            for funci in self.funcionarios:
                print(funci)


empresa = Empresa()


def menu():
    print('1-) Adicionar Funcionário')
    print('2-) Remover Funcionário')
    print('3-) Lista de Funcionários')
    print('4-) Sair')

    while True:
        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            nome = str(input('Nome: '))
            cargo = str(input('Cargo: '))
            salario = float(input('Salário: '))
            funcionario = Funcionario(nome, cargo, salario)
            empresa.adicionar_funcionario(funcionario)

        elif opcao == 2:
            nome = str(input('Nome: '))
            funcionario_encontrado = None
            for func in empresa.funcionarios:
                if func.nome == nome:
                    funcionario_encontrado = func
                    break

            if funcionario_encontrado:
                empresa.remover_funcionario(funcionario_encontrado)
            else:
                print('O funcionário não foi encontrado no Banco de Dados')


        elif opcao == 3:
            empresa.lista_funcionarios()

        elif opcao == 4:
            print('Saindo do Sistema! Até mais.')
            break
        else:
            print('Digite uma opção válida!')
            continue
menu()