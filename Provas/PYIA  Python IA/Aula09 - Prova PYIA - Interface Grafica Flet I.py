# Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário adicionar itens a uma lista de tarefas. A interface da aplicação deve incluir um campo de entrada de texto para o usuário digitar o nome da tarefa e um botão para adicionar a tarefa à lista. Quando o usuário clicar no botão, o item deve ser adicionado a uma lista exibida na tela, mostrando todas as tarefas que foram incluídas até o momento. A lista de tarefas deve ser atualizada dinamicamente sempre que um novo item for adicionado.

import flet as ft


def main(page: ft.Page):
    page.title = 'Lista de Tarefas'
    label = ft.Text('Nome da Tarefa')
    nome_tarefa = ft.TextField(hint_text="Digite sua tarefa aqui", value="")

    lista = ft.Column()

    def adicionar_tarefa(e):
        if nome_tarefa.value.strip():
            nova_tarefa = ft.Checkbox(label=nome_tarefa.value)
            lista.controls.append(nova_tarefa)
            nome_tarefa.value = ""
            page.update()
    botao = ft.ElevatedButton('Adicionar', on_click=adicionar_tarefa)

    page.add(
        label, nome_tarefa, botao, lista
    )


ft.app(target=main)
