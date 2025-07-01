# 1-) Crie um dicionário para armazenar o nome e o preço de cinco produtos.
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço.
# 2-) À medida que o usuário fornece os dados, armazene cada produto como uma
# chave no dicionário e o preço como o valor associado a essa chave.
# 3-) Após a inserção de todos os produtos e preços, calcule o valor total da
# compra somando todos os preços armazenados no dicionário.
# 4-) Por fim, exiba o valor total da compra.

nome_preco = {}

confirmacao = str(input('Você que adicionar algum produto.\n*sim ou nao\n '))
quantidade = int(input('Quantidade de produtos que vai adicionar: '))

soma = 0

if confirmacao.lower() == 'sim':
    for cont in range(quantidade):
        if quantidade > 0:
            nome = str(input('Nome do produto:  '))
            preco = float(input('Preço do produto: '))
            nome_preco[nome] = preco
    for chave, valor in nome_preco.items():
        soma += valor
elif confirmacao == 'nao':
    print('Volte sempre =)')
else:
    print('Não entendi o que você quis dizer. Deslcupa! =(')

print(f'O valor total da compra foi R${soma:.2f}')
