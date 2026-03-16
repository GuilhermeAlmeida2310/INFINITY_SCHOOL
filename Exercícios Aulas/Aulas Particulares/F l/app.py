import flet as ft

# def main(page: ft.Page):
#     page.title = 'Meu primeiro Flet'
#     page.update()

#     ft.Text('Olá Mundo')
#     ft.ElevatedButton('Clique Aqui!', on_click=ao_clicar )
#     ft.TextField(label='Nome')

#     ft.Row(controls='Lista')
#     ft.Column(controls='')

#     def ao_clicar(e):
#         print('Botão Clicado')

def main(page: ft.Page):
    page.title = 'Título'

    texto = ft.Text('Clique no botão abaixo!')

    def clicar(e):
        texto.value = 'Você clicou no botão🥳!!!'
        page.update()
    
    botao = ft.ElevatedButton('Clique no Botão', on_click=clicar)

    page.add(
        texto,botao
    )

ft.app(target=main)

