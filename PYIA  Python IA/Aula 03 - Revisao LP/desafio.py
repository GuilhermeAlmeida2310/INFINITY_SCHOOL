# Você foi contratado para desenvolver um programa simples para auxiliar em um processo de compra de produtos. O programa deve permitir ao usuário inserir o nome e o preço de vários produtos, perguntando se deseja continuar inserindo mais produtos após cada entrada. Ao final, o programa deve fornecer um resumo da compra, incluindo:
# A) O total gasto na compra.
# B) A quantidade de produtos que custam mais de R$1000.
# C) O nome do produto mais barato.
# Desenvolva o programa em Python utilizando conceitos de entrada/saída de dados, condicionais e laços de repetição.

total = []
mais_de_1000 = 0
mais_barato = None
menor_preco = None
produtos = []

while True:
    produto = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: '))
    produtos.append({'Nome': produto, 'Preço': preco})
    total.append(preco)

    if preco > 1000:
        mais_de_1000 += 1

    if menor_preco is None or preco < menor_preco:
        menor_preco = preco
        mais_barato = produto

    print('''
Opções.
1-) Sim
2-) Não''')

    opcao = int(input('Você deseja adicionar mais produtos? '))

    if opcao == 1:
        continue
    elif opcao == 2:
        break
    else:
        print('Digite uma opção válida!')

print(f'''O valor total da compra é R${sum(total):.2f}
Quantidade de produtos que valem mais de R$1000: {mais_de_1000}
Produto mais barato: {mais_barato} R${menor_preco:.2f}''')
