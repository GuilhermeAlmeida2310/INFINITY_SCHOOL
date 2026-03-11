# Crie uma função chamada media que receberá três números como argumentos. Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.

def media(num1: float, num2: float, num3: float):
    media = (num1 + num2 + num3) / 3
    return media


lista = []

for cont in range(3):
    numeros = float(input('Digite sua nota: '))
    lista.append(numeros)
print(media(lista[0], lista[1], lista[2]))
