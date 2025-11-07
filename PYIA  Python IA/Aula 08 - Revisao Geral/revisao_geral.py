# Atividade 01.
# Dada uma lista de números, crie uma nova lista contendo apenas os números pares.

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []

for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)
print(f'Sua lista de números pares é composta por {pares}')

# Atividade 02.
# Crie um dicionário com informações de produtos, incluindo nome, preço e quantidade em estoque. Implemente funções para adicionar, remover e atualizar produtos no dicionário.

produtos = [{'Nome': 'Arroz', 'Preço': 20, 'Quantidade': 30},
            {'Nome': 'Feijão', 'Preço': 10, 'Quantidade': 25},
            {'Nome': 'Carne', 'Preço': 45, 'Quantidade': 30}
            ]


def adicionar_produto():
    produto = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: '))
    quantidade = int(input('Insira a quantidade do produto: '))
    print('O produto foi adicionado ao estoque!')
    print(f'''Nome: {produto}|Preço: R${preco:.2f}|Quantidade: {quantidade}''')
    print(' ')
    produtos.append(
        f'Nome: {produto}, Preço: R${preco:.2f}, Quantidade: {quantidade}')

def remover_produto():
    for indice, produto in enumerate(produtos):
        print(f'{indice} - {produto}')
    posicao = int(input('Insira a posição do produto: '))
    produtos.pop(posicao)
    print('O produto foi removido com sucesso!')

def atualizar_produto():
    for indice, produto in enumerate(produtos):
        print(f'{indice} - {produto}')
    posicao = int(input('Insira a posição do produto: '))
    produto_escolhido = produtos[posicao]
    print('O que você deseja atualizar?')
    print('0-) Nome')
    print('1-) Preço')
    print('2-) Quantidade')
    campo = int(input('Insira um número para atualizar o campo: '))
    novo_valor = input("Digite o novo valor: ")
    if campo == 0:
        produto_escolhido['Nome'] = novo_valor
    elif campo == 1:
        produto_escolhido['Preço'] = float(novo_valor)
    elif campo == 2:
        produto_escolhido['Quantidade'] = int(novo_valor)
    print('Produto atualizado:', produto_escolhido)

def ver_produtos():
    print(produtos)

def menu_opcoes():
    print('1-) Adicionar Produto')
    print('2-) Remover Produto')
    print('3-) Atualizar Produto')
    print('4-) Ver Produtos')
    print('5-) Sair')

while True:
    menu_opcoes()
    opcao = int(input('Escolha sua opção: '))

    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        remover_produto()
    elif opcao == 3:
        atualizar_produto()
    elif opcao == 4:
        ver_produtos()
    elif opcao == 5:
        print('Encerrando o programa. Até mais!')
        break
    else:
        print('Escolha uma opção válida!')
        continue

# Atividade 03.
# Crie um conjunto com nomes de cores. Implemente uma função que retorne as cores que têm mais de quatro letras.

cores = {'Azul','Vermelho','Preto','Amarelo','Roxo','Verde'}

def maior_que_4():
    for letra in cores:
        if len(letra) > 4:
            print(letra)

maior_que_4()

# Atividade 04.
# Crie uma função que receba uma lista de strings e retorne uma nova lista contendo apenas as strings palíndromos.

def strings():
    palindromos = []
    quantidade = int(input('Quantas palavras você quer digitar? '))
    for i in range(quantidade):
        palavra = str(input('Digite uma palavra: '))
        palavra = palavra.lower()
        if palavra == palavra[::-1]:
            palindromos.append(palavra)
    return palindromos

print(strings())

# Atividade 05.
# Dado um dicionário que representa as vendas de produtos, encontre o produto mais vendido (ou os produtos mais vendidos, se houver um empate).

gerencia = {}

while True:
    produto = input('Digite o nome do produto: ').capitalize()
    vendas = int(input('Digite a quantidade de vendas: '))

    gerencia[produto] = vendas

    s_ou_n = input('Você quer adicionar mais produtos? ').capitalize()

    if s_ou_n == 'Sim':
        continue
    elif s_ou_n in ['Não','Nao']:
        break
    else:
        print('Digite Sim ou Não!')
        continue

max_vendas = max(gerencia.values())

produtos_mais_vendidos = [chave for chave, valor in gerencia.items() if valor == max_vendas]

print(f'Produto(s) mais vendido(s): {produtos_mais_vendidos}')
print(f'Quantidade de vendas: {max_vendas}')

# Atividade 06.
# Receba uma lista de números e use funções agregadoras para contar quantos valores são ímpares e quantos são pares.

lista = []
quantidade = int(input('Insira quantos números você quer verificar: '))

for cont in range(quantidade):
    numeros = int(input('Digite o número: '))
    lista.append(numeros)

def pares():
    pares = []
    for numero in lista:
        if numero %2 == 0:
            pares.append(numero)
    print(f'Quantidade de números pares: {len(pares)}')

def impares():
    impares = []
    for numero in lista:
        if numero %2 == 1:
            impares.append(numero)
    print(f'Quantidade de números impares: {len(impares)}')

pares()
impares()