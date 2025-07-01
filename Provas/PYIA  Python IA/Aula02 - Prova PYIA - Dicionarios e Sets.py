# 1-) Crie um dicionário que irá armazenar informações de um contato, incluindo o nome,
# o telefone e o email.
# 2-) Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato,
# o número de telefone e o endereço de email.
# 3-) Após coletar todas as informações necessárias, exiba o conteúdo do dicionário,
# mostrando todas as informações do contato inserido pelo usuário.

nome = str(input('Informe seu nome aqui: '))
telefone = int(input('Informe seu número de telefone aqui: '))
email = str(input('Informe seu email aqui: '))

dados = {'Nome': nome, 'Telefone': telefone, 'Email': email}
print(dados)
