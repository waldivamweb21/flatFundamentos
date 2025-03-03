import flet as ft

def main(page:ft.Page):
    msg = ft.Text(value="Olá Mundo!")
    page.add(msg)

ft.app(target=main)
