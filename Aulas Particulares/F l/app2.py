import flet as ft

def main(page: ft.Page):
    page.title = 'Formulário de Cadastro'
    nome = ft.TextField(label='Nome')
    sobrenome = ft.TextField(label='Sobrenome')
    email = ft.TextField(label='Email',keyboard_type=ft.KeyboardType.EMAIL)

    resultado = ft.Text()

    def enviar(e):
        resultado.value = f'Cadastro de {nome.value} {sobrenome.value} com o email {email.value} realizado'
        page.update()

    botao = ft.ElevatedButton('Clique no botão para enviar',on_click=enviar)

    page.add(
        nome,sobrenome,email,botao,resultado
    )

ft.app(target=main)