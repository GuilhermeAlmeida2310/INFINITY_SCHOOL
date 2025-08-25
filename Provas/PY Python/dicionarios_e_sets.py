# Crie um sistema de login que armazene usuários e senhas em um dicionário.
# O programa deve verificar se o usuário existe e se a senha está correta.

usuarios = {}

quantidade = int(input('Insira o número de pessoas que serão cadastradas: '))

for i in range(quantidade):
    usuario = str(input('Digite o nome: '))
    senha = str(input('Digite a senha: '))
    usuarios[usuario] = senha

print(usuarios)

while True:
    nome = str(input('Digite seu nome de usuário: '))

    if nome in usuarios:
        print('O usuário está cadastrado!')
        login = str(input('Digite sua senha: '))
        if login == usuarios[nome]:
            print(f'Bem-vindo de volta {nome}')
            break
        else:
            print('Senha incorreta!')

    else:
        print('Essa pessoa não possuí cadastro!')
