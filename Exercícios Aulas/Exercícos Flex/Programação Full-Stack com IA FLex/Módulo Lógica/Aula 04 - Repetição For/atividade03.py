# Crie um programa que peça ao usuário uma palavra e, usando um loop for, conte quantas vogais existem nessa palavra. Ao final, exiba a quantidade total de vogais encontradas.

palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print("Quantidade de vogais:", contador)