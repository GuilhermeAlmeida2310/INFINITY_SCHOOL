# Função I
# Atividade 1.
# def saudacao(nome):
#     printf'Bem-vindo {nome}'
# saudacao('Guilherme')

# Atividade 2.
# def saudacao_horario(hora):
#     if hora >= 5 and hora <= 12:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 18:
#         print('Boa tarde')
#     else:
#         print('Boa noite')
# saudacao_horario(1)

# Atividade 3.
# def soma(num1,num2):
#     return num1 + num2
# print(soma(6,4))

# Atividade 4.
# def subtracao(num1,num2):
#     return num1 - num2
# print(subtracao(6,4))

# Atividade 5
# def multiplicacao(num1,num2):
#     return num1 * num2
# print(multiplicacao(6,4))

# DESAFIO!!!
# def soma(num1,num2):
#     return num1 + num2

# def subtracao(num1,num2):
#     return num1 - num2

# def multiplicacao(num1,num2):
#     return num1 * num2

# def divisao(num1,num2):
#     return num1 / num2

# def menu_opcoes():
#     print('Calculadora')
#     print('1-) Somar')
#     print('2-) Subtrair')
#     print('3-) Multiplicar')
#     print('4-) Dividir')
#     print('5-) Sair')

# while True:
#     menu_opcoes()
#     opcao = int(input('Escolha uma opção: '))

#     if opcao == 5:
#         print('Encerrando a calculadora.')
#         break
    
#     num1 = float(input('Digite o primeiro número: '))
#     num2 = float(input('Digite o segundo número: '))

#     if opcao == 1:
#         print(f'Resultado da conta: {num1+num2}')
#     elif opcao == 2:
#         print(f'Resultado da conta: {num1-num2}')
#     elif opcao == 3:
#         print(f'Resultado da conta: {num1*num2}')
#     elif opcao == 4:
#         print(f'Resultado da conta: {num1/num2}')
#     else:
#         print('Digite uma opção válida.')

# Função II
# Atividade 1.

# nota1 = float(input('Insira sua nota: '))
# nota2 = float(input('Insira sua nota: '))
# nota3 = float(input('Insira sua nota: '))

# def media(nota1,nota2,nota3):
#     soma = nota1 + nota2 + nota3
#     return soma / 3


# print(media(nota1,nota2,nota3))

# Atividade 2.
# def retangulo(comprimento,largura):
#     area = comprimento * largura
#     return area
# print(retangulo(5,10))

# Atividade 3.
# def concatenar_string(*args):
#     resultado = ''
#     for palavra in args:
#         resultado += palavra
#     return resultado

# texto = concatenar_string('Olá',' ','Pessoal')
# print(texto)

# Atividade 4.
# def dobrar_lista(lista):
#     return list(map(lambda x: x*2, lista))

# numeros = [1,2,3,4,5]
# resultado = dobrar_lista(numeros)

# print(resultado)

