lista_compras = []

quantidade = int(input("Quantos itens deseja adicionar à lista de compras? "))

for i in range(quantidade):
    item = input(f"Digite o nome do item {i+1}: ")
    lista_compras.append(item)

print("Lista de compras:")
print(lista_compras)

remover = input("Deseja remover algum item? (sim/nao) ").lower()
if remover == "sim":
    item_remover = input("Digite o nome do item a remover: ")
    if item_remover in lista_compras:
        lista_compras.remove(item_remover)
        print("Item removido. Lista atualizada:")
        print(lista_compras)
    else:
        print("Item não encontrado na lista.")