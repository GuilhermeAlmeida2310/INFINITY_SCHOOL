# Atividade 02.
# Crie um módulo chamado manipulacao_strings que contenha funções para realizar operações com strings, como inverter uma string, contar o número de palavras em uma string e verificar se uma string é um palíndromo (lê-se igual de trás para frente). Crie um programa principal que importe o módulo e use essas funções com strings fornecidas pelo usuário.

def inverter(palavra):
    return palavra[::-1]


def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)


def palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]
