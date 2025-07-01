
tarefas = []


def add_tarefa(tarefas, nome_tarefa):
    tarefa = {
        "tarefa": nome_tarefa,
        "status": False
    }
    tarefas.append(tarefa)
    print(f'A tarefa {nome_tarefa} foi adicionada a sua lista!')
    return


def ver_tarefas(tarefas):
    print('Lista de tarefas:')
    for cont, tarefa in enumerate(tarefas, start=1):
        status = 'X' if tarefa["status"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f'{cont}. [{status}] {nome_tarefa}')
    return


def atualizar_tarefas(tarefas, indice_tarefa, atualizar_nome):
    indice_tarefa_ajustado = indice_tarefa - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = atualizar_nome
        print(f'A tarefa {indice_tarefa} foi trocada para {atualizar_nome}')
    else:
        print('O indice é inválido!')
    return


def concluir_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["status"] = True
        print(f'A tarefa {indice_tarefa} foi completa!')
    else:
        print('O indice é inválido!')
    return


def excluir_tarefas_completas(tarefas):
    for tarefa in tarefas:
        if tarefa["status"] == True:
            tarefas.remove(tarefa)
    print('As tarefas completas foram apagadas da sua lista. ')
    return


while True:
    print('''Lista de Tarefas:
          ''')
    print('1-) Adicionar Tarefa')
    print('2-) Ver Tarefas')
    print('3-) Atualizar Tarefa')
    print('4-) Concluir Tarefa')
    print('5-) Excluir Tarefas Concluídas')
    print('''6-) Sair
          ''')
    escolha = input('''O que você quer fazer? ''')
    if escolha == '1':
        nome_tarefa = input('Insira o nome da sua nova tarefa: ')
        add_tarefa(tarefas, nome_tarefa)

    elif escolha == '2':
        ver_tarefas(tarefas)

    elif escolha == '3':
        ver_tarefas(tarefas)
        indice_tarefa = int(
            input('Insira o número da tarefa que você quer atualizar: '))
        atualizar_nome = input('Insira o novo nome da tarefa: ')
        atualizar_tarefas(tarefas, indice_tarefa, atualizar_nome)

    elif escolha == '4':
        ver_tarefas(tarefas)
        indice_tarefa = int(
            input('Insira o número da tarefa que você completou: '))
        concluir_tarefa(tarefas, indice_tarefa)

    elif escolha == '5':
        excluir_tarefas_completas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == '6':
        break
print('Você saiu do programa. Até a próxima.')
