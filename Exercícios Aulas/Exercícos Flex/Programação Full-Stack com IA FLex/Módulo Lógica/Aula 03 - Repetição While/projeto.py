contador_vendas = 0
total_vendas = 0

valor = float(input("Digite o valor da venda (0 para encerrar o dia): "))

while valor != 0:
    total_vendas += valor
    contador_vendas += 1
    valor = float(input("Digite o valor da próxima venda (0 para encerrar o dia): "))

if contador_vendas > 0:
    media_vendas = total_vendas / contador_vendas
    print("Número de vendas realizadas:", contador_vendas)
    print("Total arrecadado: R$", total_vendas)
    print("Valor médio por venda: R$", media_vendas)
else:
    print("Nenhuma venda foi registrada hoje.")