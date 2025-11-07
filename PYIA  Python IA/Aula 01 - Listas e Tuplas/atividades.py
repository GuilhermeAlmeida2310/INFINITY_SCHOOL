# Atividade 01.
# Faça a definição de uma lista contendo os números de 1 até 5. Finalmente, utilize o print() para exibir os valores da lista.

lista = [1,2,3,4,5]
print(lista)

# Atividade 02.
# Faça a definição de uma lista contendo as vogais. Finalmente, utilize o print() para exibir os valores da lista.

lista = ['a', 'e', 'i', 'o', 'u']
print(lista)

# Atividade 03.
# Defina uma lista com 5 itens que tenha, pelo menos, 3 classes diferentes. Utilize o print() para exibir o terceiro elemento dessa lista.

lista = [1, 2.0, 'Gato', True]
print(lista[2])

# Atividade 04.
# Crie uma tupla para representar as informações de três palestrantes, cada uma contendo o nome, o tema da palestra e a instituição à qual estão vinculados. Exiba na tela as informações do terceiro palestrante, incluindo nome, tema da palestra e instituição.

palestrantes = (('Lucas', 'O Futuro da Inteligência Artificial', 'Fatec'),
                ('Larissa', 'Como a Tecnologia Transforma Negócios', 'USP'),
                ('Henrique', 'Produtividade em Tempos Digitais', 'PUC-SP'))

print(f'''Nome do Palestrante: {palestrantes[2][0]}
Tema da Palestra: {palestrantes[2][1]}
Instituição: {palestrantes[2][2]}''')