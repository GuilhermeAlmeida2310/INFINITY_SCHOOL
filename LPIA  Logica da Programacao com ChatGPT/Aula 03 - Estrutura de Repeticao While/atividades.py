# Atividade 1.
# Crie um programa que use um laço while para contar de 1 a 10 e exibir cada número.

numero = 1
while numero <= 10:
    print(numero)
    numero += 1

# Atividade 2.
# Escreva um programa que use um laço while para somar os números de 1 a 100 e exiba o resultado.

numero = 1
soma = 0
while numero <= 100:
    soma += numero
    numero += 1
    print(soma)

# Atividade 3.
# Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10).

numero = int(input('Digite um número de 1 a 10: '))
soma = 0
while soma <= 9:
    soma += 1
    print(f'{numero} x {soma} = {numero * soma}')

# Atividade 4.
# Desenvolva um programa que use um laço while para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

numero = 10

while numero >= 1:
    print(numero)
    numero -= 1
print('FELIZ ANO NOVO!!!')


# Atividade 5.
# Crie um programa que solicite um número ao usuário e use um laço while para contar de 1 até o número inserido, exibindo apenas os números ímpares.

numero = 1
contador = int(input('Digite o número aqui: '))

while numero <= contador:
    if numero % 2 != 0:
        print(numero)
    numero += 1

# Atividade 6.
# Escreva um programa que solicite números ao usuário até que ele digite um número negativo, somando apenas os números positivos inseridos.

soma = 0
while True:
    numero = int(input('Digite o número aqui: '))

    if numero > 0:
        soma += numero
        print(soma)
    else:
        break

# Atividade 7.
# Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10), mas apenas para os resultados que forem múltiplos de 3.

numero = int(input('Digite o número aqui: '))
multiplicador = 1

while multiplicador <= 10:
    resultado = numero * multiplicador

    if resultado % 3 == 0:
        print(f'{numero} X {multiplicador} = {resultado}')

    multiplicador += 1

# Atividade 8.
# Desenvolva um programa que solicite as notas dos alunos até que o usuário digite -1. Calcule e exiba a média das notas inseridas.

soma = 0
contador = +1

while True:
    numero = float(input('Digite sua nota aqui: '))

    if numero > -1:
        soma += numero
        contador += 1
        print(f'Essa é a soma de todas notas digitadas: {soma}')
    else:
        break

if contador > 0:
    media = soma / contador
    print(f'Média da soma de todas as notas: {media}')
else:
    print('A nota inserida não é válida')

# Atividade 9
# Crie um programa que use um laço while para contar de 1 a 10 e termine quando atingir 10.

contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# Atividade 10
# Escreva um programa que use um laço while para somar números consecutivos começando de 1 e termine quando a soma atingir ou ultrapassar 50.

inicio = 1
soma = 0
while soma <= 50:
    soma += inicio
    inicio += 1
    print(soma)

# Atividade 11
# Crie um programa que solicite ao usuário um número entre 1 e 10. Continue pedindo até que o usuário forneça um valor inválido.

numero = int(input('Digite um número entre 1 e 10: '))

while True:
    if numero <= 10:
        print(int(input('Digite novamente: ')))
    else:
        print('Estr valor é inválido!')
        break

# Atividade 12.
# Desenvolva um programa que peça ao usuário para digitar uma senha e continue pedindo até que a senha correta seja inserida.

senha = str(input('Digite sua senha aqui: '))

while True:
    confirmar_senha = str(input('Digite sua senha aqui: '))
    if senha == confirmar_senha:
        print('Sua senha está correta. Bem-vindo!')
        break
    else:
        print('Sua senha está incorreta!')
        print(str(input('Digite sua senha novamente: ')))

# Atividade 13.
# Crie um programa que use um laço while para somar todos os números pares de 1 a 100 e exiba o resultado.

cont = 1
soma = 0

while cont <= 100:
    if cont % 2 == 0:
        soma += cont
    cont += 1
print(soma)

# Atividade 14
# Escreva um programa que use um laço while para exibir todos os números ímpares de 1 a 50.

cont = 1

while cont <= 50:
    if cont % 2 != 0:
        print(cont)
    cont += 1
