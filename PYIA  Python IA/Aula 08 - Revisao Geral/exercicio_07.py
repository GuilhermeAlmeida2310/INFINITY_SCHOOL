# Atividade 07.
# Você possui dados de vendas trimestrais de uma empresa em uma lista. Cada trimestre é representado como uma lista de números, onde cada número representa o valor de vendas de um mês (janeiro a março, abril a junho, julho a setembro e outubro a dezembro). Você deve realizar as seguintes tarefas: Calcule a média de vendas por trimestre. Encontre o trimestre com a maior soma de vendas. Encontre o trimestre com a menor soma de vendas. Calcule o total de vendas no ano inteiro. - Construa seus dados fictícios

vendas = [[4321, 2999, 3888],
          [4777, 3655, 2544],
          [4012, 4890, 3566],
          [4222, 3677, 2789]]


def media_trimestres():
    media_vendas = []
    for medias in vendas:
        soma = sum(medias)
        media = soma / 4
        media_vendas.append(media)
    print(f'''1º Trimestre: {media_vendas[0]:.2f}
2º Trimestre: {media_vendas[1]:.2f}
3º Trimestre: {media_vendas[2]:.2f}
4º Trimestre: {media_vendas[3]:.2f}''')
    print('')


def maior_venda():
    somas = []
    for ver_maior in vendas:
        soma = sum(ver_maior)
        somas.append(soma)
    maior = max(somas)
    indice = somas.index(maior) + 1
    print(f'{indice} Trimestre: {maior} vendas')
    print('')


def menor_venda():
    somas = []
    for ver_menor in vendas:
        soma = sum(ver_menor)
        somas.append(soma)
    menor = min(somas)
    indice = somas.index(menor) + 1
    print(f'{indice} Trimestre: {menor} vendas')
    print('')


def total_vendas():
    vendas_tri = []
    for total in vendas:
        soma = sum(total)
        vendas_tri.append(soma)
    vendas_total = sum(vendas_tri)
    print(f'Vendas totais: {vendas_total}')
    print('')


def menu():
    while True:
        print('Simulador de Comércio')
        print('1-) Média de Vendas')
        print('2-) Trimestre com mais Vendas')
        print('3-) Trimestre com menos Vendas')
        print('4-) Vendas do Ano')
        print('5-) Sair')

        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            media_trimestres()
        elif opcao == 2:
            maior_venda()
        elif opcao == 3:
            menor_venda()
        elif opcao == 4:
            total_vendas()
        elif opcao == 5:
            print('Encerrando o programa. Até mais!')
            break
        else:
            print('Digite uma opção válida!')
            print('')
            continue


menu()
