#  Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um formulário de contato. O formulário deve incluir três campos: um campo de texto para o nome, um campo de texto para o email e um campo de texto para a mensagem. Após o usuário preencher esses campos, deve haver um botão de envio. Quando o usuário clicar no botão de envio, os dados devem ser processados e uma mensagem de confirmação deve ser exibida na tela, indicando que o formulário foi enviado com sucesso.

import flet as ft


def main(page: ft.Page):
    page.title = 'Formulário de Contato'

    label1 = ft.Text('Nome')
    nome = ft.TextField(hint_text='Digite seu nome aqui')

    label2 = ft.Text('Email')
    email = ft.TextField(hint_text='Digite seu email aqui')

    label3 = ft.Text('Mensagem')
    msg = ft.TextField(hint_text='Digite sua mensagem aqui', multiline=True)

    confirmacao = ft.Text("")

    def enviar_formulario(e):
        if nome.value and email.value and msg.value:
            confirmacao.value = "O formulário foi enviado com sucesso!"
            nome.value = ""
            email.value = ""
            msg.value = ""
        else:
            confirmacao.value = "Você não preencheu todos os campos!"

        page.update()

    botao = ft.ElevatedButton("Enviar", on_click=enviar_formulario)

    page.add(
        label1, nome, label2, email, label3, msg, botao, confirmacao
    )


ft.app(target=main)
