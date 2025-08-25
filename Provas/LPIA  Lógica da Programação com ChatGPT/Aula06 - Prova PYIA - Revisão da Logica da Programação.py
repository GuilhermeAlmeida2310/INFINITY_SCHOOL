# 1-) Crie um programa em Python que simule um sistema de login.

# 2-) O programa deve permitir ao usuário três tentativas para acertar
#     o nome de usuário e a senha corretos.

# 3-) Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem
#     informando quantas tentativas restam.

# 4-) Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida,
#     e o programa deve terminar imediatamente.

# 5-) Se todas as três tentativas falharem, o programa deve usar um loop for
#     para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

nome_usuario = str(input('Digite seu nome de usuário: '))
senha = str(input('Digite seu senha: '))
tentativas = 3

for cont in range(3):
    confirmacao_nome = str(input('Confirme sue nome de usuário: '))
    confirmacao_senha = str(input('Confirme sua senha: '))
    if confirmacao_nome == nome_usuario and confirmacao_senha == senha:
        print('''Os dados estão corretos
Bem vindo de volta!''')
        break
    else:
        tentativas -= 1
        print('Usuário ou senha incorretos.')
        print(f'Tentativas restantes:{tentativas}')
else:
    print('Acesso negado!')
