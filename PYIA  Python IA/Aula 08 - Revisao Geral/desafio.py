# DESAFIO!!!
# Você tem um conjunto de dados que contém informações sobre a produção anual de diferentes culturas em diversas fazendas ao longo de vários anos. O objetivo é realizar uma análise simples desses dados usando apenas as funções agregadoras.
# Tarefas: Encontre o ano em que a produção total foi máxima e o ano em que foi mínima. Identifique a cultura que teve a maior produção total e a cultura com a menor produção total ao longo dos anos. Encontre a fazenda que obteve a produção máxima em um determinado ano e a fazenda com a produção mínima no mesmo ano. - Construa seus próprios dados fictícios.

dados = {
    2022: {
        'Fazenda A': {'Holanda': 5000, 'Japão': 4000},
        'Fazenda B': {'Brasil': 4500, 'Estados Unidos': 3000}
    },
    2023: {
        'Fazenda A': {'Holanda': 4000, 'Japão': 3500},
        'Fazenda B': {'Brasil': 5500, 'Estados Unidos': 4000}
    },
    2024: {
        'Fazenda A': {'Holanda': 4500, 'Japão': 4000},
        'Fazenda B': {'Brasil': 4500, 'Estados Unidos': 5000}
    }
}

total_2022 = 0
total_2023 = 0
total_2024 = 0

dicio_paises = {}

for anos, fazendas in dados.items():
    for paises in fazendas.values():
        for vendas in paises.values():
            if anos == 2022:
                total_2022 += vendas
            elif anos == 2023:
                total_2023 += vendas
            else:
                total_2024 += vendas

totais = {2022: total_2022, 2023: total_2023, 2024: total_2024}

for anos, fazendas in dados.items():
    for paises in fazendas.values():
        for pais, vendas in paises.items():
            if pais not in dicio_paises:
                dicio_paises[pais] = vendas
            else:
                dicio_paises[pais] += vendas

maior_venda = max(totais, key=totais.get)
menor_venda = min(totais, key=totais.get)
print(f'Ano com maior venda: {maior_venda}')
print(f'Ano com menor venda: {menor_venda}')

maior_pais = max(dicio_paises, key=dicio_paises.get)
menor_pais = min(dicio_paises, key=dicio_paises.get)
print(f'Ano com maior produção: {maior_pais}')
print(f'Ano com menor produção: {menor_pais}')
