contador = 0
soma = 0

while contador < 5:
    numero = int(input(f"Digite o {contador + 1}º número: "))
    soma += numero
    contador += 1

media = soma / contador

print("Média dos números:", media)