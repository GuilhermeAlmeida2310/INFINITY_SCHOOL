nomes = []
notas = []

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota: "))
    nomes.append(nome)
    notas.append(nota)

print("Nome\t\tNota\tSituação")
print("-"*30)
for i in range(len(nomes)):
    media = notas[i]
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    print(f"{nomes[i]:<10}\t{media:<5}\t{situacao}")