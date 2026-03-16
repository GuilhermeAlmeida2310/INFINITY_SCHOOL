# Crie um dicionário vendas que armazena o número de vendas por vendedor.As chaves são os nomes e os valores são as vendas (ex: {"Ana": 10, "Bruno": 15, "Carla": 8}). Adicione um novo vendedor, "Pedro", com 12 vendas. Depois, remova a vendedora "Carla" do dicionário. Por fim, calcule e imprima a soma total de todas as vendas restantes.

vendas = {"Ana": 10, "Bruno": 15, "Carla": 8}
vendas["Pedro"] = 12
del vendas["Carla"]
total_vendas = sum(vendas.values())
print(f"A soma total das vendas é: {total_vendas}")