# Atividade 1.
# Crie um programa que solicita ao usuário que insira três notas e, em seguida, calcule a média dessas notas usando uma função. A função deve receber as três notas como argumentos e retornar a média. Por fim, o programa deve imprimir a média calculada.

soma = 0
for i in range(3):
    nota = float(input('Insira sua nota: '))
    soma += nota

def media(soma):
    return soma / 3

print(media(soma))

# Atividade 2.
# Crie um programa que define uma função chamada "calcular_area_retangulo", que recebe dois argumentos, comprimento e largura e, retorna a área desse retângulo. Em seguida,o programa deve solicitar ao usuário que insira o comprimento e a largura largura e imprimir a área calculada.

comprimento = float(input('Insira o comprimento da área: '))
largura = float(input('Insira a largura da área: '))

def calcular_area_retangulo(comprimento,largura):
    area = comprimento * largura
    return area
print(calcular_area_retangulo(comprimento,largura))

# Atividade 3.
# Crie uma função chamada 'concatenar_strings' que aceita um número variável de strings como argumentos posicionais (usando *args) A função deve concatenar todas as strings em uma única string e retorná-la.

def concatenar_strings(*args):
    return ', '.join(args)
print(concatenar_strings('gato', 'cachorro', 'coelho'))

# Atividade 4.
# Crie uma função que aceita uma lista de números e use a função map para retornar uma nova lista contendo o dobro de cada número na lista de entrada

def duplicar(numero):
    return numero * 2

def numeros(lista):
    resultado = map(duplicar,lista)
    return list(resultado)

print(numeros([1,2,3,4,5]))

# Atividade 5.
# Crie uma função que aceita uma lista de números e use a função filter para retornar uma nova lista contento apenas os números pares da lista de entrada

def numeros(lista):
    return list(filter(lambda x: x %2 == 0,lista))
print(numeros([1,2,3,4,5,6,7,8,9,10]))

# Atividade 6.
# Crie uma função que aceita uma lista de strings e use a função reduce (importada de functools) para encontrar a maior string na lista.

from functools import reduce

def strings(lista):
    return reduce(lambda a,b: a if len(a) > len(b) else b, lista)

print(strings(['Oi', 'Gato']))

# # Atividade 7.
# Crie uma função chamada criar_lista_de_compras que aceita um número variável de itens de compras como argumentos posicionais (usando *args). A função deve criar e retornar uma lista de compras que contenha todos os itens fornecidos.

def criar_lista_de_compras(*args):
    return args
criar_lista_de_compras()

print(criar_lista_de_compras('Arroz,','Feijão','Macarrõa','Café'))

# Atividade 8.
# Crie uma função que aceite dois números e uma operação por exemplo: adição, subtração, multiplicação, divisão. Use como argumentos e funções lambda para realizar a operação especificada. A função deve retornar o resultado da operação.

def somar(num1,num2):
    soma = lambda : num1 + num2
    return soma()
somar(5,5)
print(somar(5,5))