import flet as ft


def main(page: ft.Page):
    page.title = 'Lista de Tarefas'
    label = ft.Text('Nome da Tarefa')
    nome_tarefa = ft.TextField('')

    lista = ft.Column()

    def adicionar_tarefa(e):
        if nome_tarefa.value:
            nova_tarefa = ft.Checkbox(label=nome_tarefa.value)
            lista.controls.append(nova_tarefa)
            nome_tarefa.value = ''
            page.update()
    botao = ft.ElevatedButton('Adicionar', on_click=adicionar_tarefa)

    page.add(
        label, nome_tarefa, botao, lista
    )


ft.app(target=main)
