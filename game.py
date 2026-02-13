import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha a opção correta")
    resposta_correta = "Gato"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Parabéns!"
        else:
            mensagem.value = "Resposta Errada"
            page.update()

        # page.add(ft.Text(e.control.content))

    page.title = "Game: Adivinhe a Imagem!!"
    page.bgcolor = "#e0a3ff"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe a Imagem!!",
                    size= 24,
                    weight="bold"
                ),
                ft.Image(
                    src="images/gatinho.jpg",
                    height=200
                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="Cachorro",
                            bgcolor="purple",
                            color="white",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Gato",
                            bgcolor="purple",
                            color="white",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Coelho",
                            bgcolor="purple",
                            color="white",
                            on_click=verificar_resposta
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                mensagem
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)