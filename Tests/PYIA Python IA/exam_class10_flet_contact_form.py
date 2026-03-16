import flet as ft

def main(page: ft.Page):
    page.title = 'Contact Form'

    label1 = ft.Text('Name')
    name = ft.TextField(hint_text='Insert your name')

    label2 = ft.Text('Email')
    email = ft.TextField(hint_text='Insert your email')

    label3 = ft.Text('Message')
    message = ft.TextField(hint_text='Insert your message', multiline=True)

    confirmation = ft.Text('')

    def share_form(e):
        if name.value and email.value and message.value:
            confirmation.value = 'The form was sent with success!'
            name.value = ''
            email.value = ''
            message.value = ''

        else:
            confirmation.value = 'Please fill in all fields!'

        page.update()

    buttom = ft.ElevatedButton('Sent', on_click=share_form)

    page.add(
        label1, name, label2, email, label3, message, buttom, confirmation
    )

ft.app(target=main)