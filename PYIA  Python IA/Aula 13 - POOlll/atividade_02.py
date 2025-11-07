# Desenvolva uma aplicação de loja online em. Crie as classes Cliente e Pedido com uma associação bidirecional. Os clientes podem fazer pedidos, e os pedidos devem estar associados aos clientes que os fizeram. Implemente a capacidade de listar todos os pedidos de um cliente específico.

class Cliente:
    def fazer_pedido(self):
        pedidos = {}
        pessoas = int(input('Insira quantas pessoas vão fazer compras: '))
        for i in range(pessoas):
            nome = str(input('Insira seu nome: '))
            quantidade = int(input('Digite quantos pedidos você quer fazer: '))
            for j in range(quantidade):
                produtos = str(input('Digite o nome do seu produto: '))
                qtd_pedido = int(
                    input('Insira quantas unidades você vai comprar: '))
                if nome not in pedidos:
                    pedidos['Cliente'] = nome
                    pedidos[produtos] = qtd_pedido
                    pedidos.update()

        return pedidos


cliente = Cliente()
print(cliente.fazer_pedido())
