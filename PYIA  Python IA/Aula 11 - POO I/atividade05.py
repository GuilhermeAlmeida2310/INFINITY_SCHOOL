# Crie uma classe chamada Fatura , a classe Fatura deve incluir os seguintes atributos o nome do item; o preço unitário do item; quantidade de item a ser faturado; valor total da fatura; Sua classe deve ter um construtor que inicialize todos os atributos menos o valor total da fatura. Forneça um método chamado gerar_fatura que calcula o valor da fatura (isto é, multiplicar a quantidade pelo preço por item).

produtos = []
preco_total = []


class Fatura:
    def __init__(self, nome_item, preco, qtd):
        self.nome_item = nome_item
        self.preco = preco
        self.qtd = qtd

    def __repr__(self):
        return f'''Nome: {self.nome_item} | Quantidade: {self.qtd} | Preço: R${self.preco} |'''

    def gerar_fatura(self):
        return self.preco * self.qtd


def menu():
    print('Fatura')
    print('1-) Adicionar Produtos')
    print('2-) Calcular Fatura')
    print('3-) Ver Fatura')
    print('4-) Sair')

    total = 0

    while True:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            quantidade = int(input('Quantos produtos você vai adicionar: '))
            for i in range(quantidade):
                nome_produto = str(input('Nome do Produto: '))
                preco = float(input('Preço do Produto: '))
                qtd = int(input('Quantidade do Produto: '))
                produto = Fatura(nome_produto, preco, qtd)
                total_preco = produto.gerar_fatura()
                produtos.append(produto)
                preco_total.append(total_preco)
            total = sum(preco_total)
        elif opcao == 2:
            total = sum(preco_total)
            print(f'Sua compra deu R${total}')

        elif opcao == 3:
            print(f'''Lista de Compras. {produtos}
Total: R${total}''')
        elif opcao == 4:
            break
        else:
            print('Insira uma opção válida!')
            continue


menu()
