# Atividade 1.
# Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).

num = int(input('Digite um número para mostrar sua tabuada: '))
cont = 0
for cont in range(0, 10):
    cont += 1
    print(f'{num} X {cont} = {num * cont}')

# Atividade 2.
# Crie um programa que use um laço for para somar todos os números de 1 a 100 e exiba o resultado.

soma = 0
for cont in range(0, 101, 1):
    soma += cont
    print(f'A soma de todos os números de 1 até 100 é igual a {soma}')

# Atividade 3
# Escreva um programa que solicite uma palavra ao usuário e use um laço for para exibir cada caractere da palavra em uma linha separada.

palavra = str(input('Digite qualquer palavra aqui: '))

for letra in palavra:
    print(letra)

# Atividade 4
# Desenvolva um programa que use um laço for para fazer uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

for cont in range(10, 0, -1):
    print(cont)
print('FELIZ ANO NOVO!!!')

# Atividade 5.
# Escreva um programa que solicite ao usuário 10 números e use um laço for com uma condicional para contar quantos são positivos e quantos são negativos.

positivos = 0
negativos = 0

for cont in range(10):
    numeros = int(
        input('Digite 10 números e verifique se são positivos ou negativos: '))

    if numeros > 0:
        print('O número que você digitou é positivo!')
        positivos += 1
    else:
        print('O número que você digitou é negativo!')
        negativos += 1

print(f'''Total de números positivos: {positivos}
Total de números negativos: {negativos}''')

# Atividade 6.
# Escreva um programa que use um laço for para somar todos os números pares de 1 a 50 e exiba o resultado final.

soma = 0
for cont in range(0, 51, 2):
    soma += cont
print(f'A soma dos números pares de 1 a 50 resulta em: {soma}')

# Atividade 7.
# Crie um programa que solicite uma palavra ao usuário e use um laço for com uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.

palavra = str(input('Digite uma palavra e veja quantas vogais tem: '))
contador_vogais = 0

for caracter in palavra:
    if caracter in 'aeiou':
        contador_vogais += 1
print(f'Número de vogais na palavra inserida = {contador_vogais}')

# Atividade 8.
# Escreva um programa que solicite 5 notas de alunos. Use um laço for para somar as notas e uma condicional para exibir a média e a classificação ("Aprovado" para média >= 6, "Reprovado" para média < 6).

soma = 0

for cont in range(5):
    nota = float(input('Digite sua nota aqui: '))
    soma += nota
    print(soma)
    media = soma / 5
print(f'Sua média final é {media}')

if media > 6:
    print('Aprovado!')
else:
    print('Reprovado!')

# Atividade 9.
# Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.

for cont in range(21):
    if cont % 2 == 0:
        print(f'{cont} Número par')
    else:
        print(f'{cont} Número ímpar')
        if cont == 15:
            break

# Atividade 10.
# Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.

positivos = 0
negativos = 0

for cont in range(10):
    numero = int(input('Insira o número: '))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        break

print(f'''Total de números positivos: {positivos}
Total de números negativos: {negativos}''')

# Atividade 11.
# Escreva um programa que use um laço for para imprimir números de 1 a 30. Use uma condicional para verificar se um número é múltiplo de 5 e outro para verificar se é maior que 20 e interromper o loop com break.

for cont in range(1, 31):
    if cont > 20:
        break
    if cont % 5 == 0:
        print(f'{cont} é Múltiplo de 5')

# Atividade 12.
# Peça ao usuário para inserir 5 preços de produtos. Use um laço for para calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e interrompa o loop com break.

soma = 0
desconto = 0
preco_total = 0

for cont in range(5):
    preco = float(input('Insira o preço do produto: '))
    soma += preco
    if soma > 100:
        desconto = soma * 0.10
        preco_total = soma - desconto
        print(f'O valor total da compra foi de R${preco_total:.2f}.')
        break
else:
    print(f'O valor total da compra foi de R${soma:.2f}.')
