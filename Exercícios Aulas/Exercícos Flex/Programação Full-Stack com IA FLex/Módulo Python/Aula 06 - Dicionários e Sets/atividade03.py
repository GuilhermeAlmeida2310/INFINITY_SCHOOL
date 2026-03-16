# Crie um dicionário que mapeia países a suas populações
#  (use pelo menos 4 países). Use o método .items() em um laço para encontrar 
#   e imprimir o país com a maior população.

# Resposta
populacoes = {"Brasil": 215_000_000, "China": 1_400_000_000, "EUA": 333_000_000, "Índia": 1_220_000_000}
pais_maior_pop = ""
maior_pop = 0
for pais, populacao in populacoes.items():
    if populacao > maior_pop:
        maior_pop = populacao
        pais_maior_pop = pais
print(f"O país com a maior população é: {pais_maior_pop} com {maior_pop} habitantes.")