# Crie um programa que cadastre alguns produtos e suas quantidades. Primeiro, pergunte quantos produtos o usuário deseja cadastrar. Em seguida, use um laço for para repetir o pedido do nome e da quantidade do produto o número de vezes informado. Durante o laço, mostre na tela cada produto cadastrado no formato: Produto: X | Quantidade: Y

quantidade = int(input('Insira o número de produtos que você deseja cadastrar: '))

for i in range(quantidade):
    produto = input('Insira o nome do produto: ')
    qtd_produto = int(input('Insira a quantidade do produto: '))
    print(f'Produto: {produto} | Quantidade: {qtd_produto}')