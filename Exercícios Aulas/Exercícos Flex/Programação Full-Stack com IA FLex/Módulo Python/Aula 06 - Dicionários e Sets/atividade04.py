# Cadastro de Produtos
# Imagine que você está criando um sistema de estoque. Crie um dicionário chamado estoque com duas chaves, "produto_a" e "produto_b", cada uma com um valor numérico de quantidade. Em seguida, adicione um novo produto, "produto_c", com a quantidade de 30. Depois, simule uma venda, diminuindo a quantidade do "produto_a" em 5.
# Imprima o dicionário final.

estoque = {"produto_a": 100, "produto_b": 50}
estoque["produto_c"] = 30
estoque["produto_a"] -= 5
print(estoque)