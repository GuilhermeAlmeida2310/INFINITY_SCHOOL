import flet as ft

def main(page: ft.Page):
    page.title = 'Task List'
    label = ft.Text('Task Name')
    task_name = ft.TextField(hint_text="Insert your task", value="")

    task_list = ft.Column()

    def add_task(e):
        if task_name.value.strip():
            new_task = ft.Checkbox(label=task_name.value)
            task_list.controls.append(new_task)
            task_name.value = ""
            page.update()
    buttom = ft.ElevatedButton('Add', on_click=add_task)

    page.add(
        label, task_name, buttom, task_list
    )

ft.app(target=main)