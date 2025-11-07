# DESAFIO!!!
# Passo 1.
# Crie um processador de texto simples que realiza várias operações em um texto de entrada, como contar palavras, contar letras, inverter o texto e substituir palavras-chave.

# Passo 2.
# A função deve aceitar uma série de operações como argumentos de palavra-chave, usando **kwargs. As operações podem incluir "contar_palavras","contar_letras","inverter_texto"e "substituir_palavra". Use funções lambda para realizar as operações de acordo com as palavras-chave especificadas nos argumentos de palavra-chave.

# Passo 3.
# Se a operação "substituir_palavra" for especificada, a função deve aceitar uma palavra-chave adicional, como "substituir_palavra" e "nova_palavra", para realizar a substituição em todo o texto A função deve retornar o texto resultante após todas as operações.

# Requisitos:
# Crie uma função chamada processador_texto que aceite uma string de texto como argumento.

def processador_texto(texto, **kwargs):
    if 'contar_palavras' in kwargs and kwargs['contar_palavras']:
        contar_palavras = lambda texto: len(texto.split())
        print(f'Número de Palavras: {contar_palavras(texto)}')
    elif 'contar_letras' in kwargs and kwargs['contar_letras']:
        contar_letras = lambda texto: len(texto.replace(" ", ""))
        print(f'Número de Letras: {contar_letras(texto)}')
    elif 'inverter_texto' in kwargs and kwargs['inverter_texto']:
        inverter_texto = lambda texto: texto[::-1]
        print(f'Texto Invertido: {inverter_texto(texto)}')
    elif 'substituir_palavra' in kwargs and kwargs['substituir_palavra']:
        novo_texto = kwargs.get('novo_texto', '')
        trocar_palavra = lambda texto: texto.replace(kwargs['trocar_palavra'], novo_texto)
        print(f'Palavra Trocada: {trocar_palavra(texto)}')
    else:
        print("Escolha uma opção válida!")

processador_texto("Hello World", contar_palavras=True)
processador_texto("Hello World", contar_letras=True)
processador_texto("Hello World", inverter_texto=True)
processador_texto("Hello World", substituir_palavra=True, trocar_palavra="World", novo_texto="universo")