import flet as ft

def main(page: ft.Page):
    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.AMBER_500,
                )
            )
        return items

    def column_with_alignment(align: ft.MainAxisAlignment):
        return ft.Column(
            [
                ft.Text(str(align), size=10),
                ft.Container(
                    content=ft.Column(items(3), alignment=align),
                    bgcolor=ft.colors.AMBER_100,
                    height=400,
                ),
            ]
        )

    page.add(
        ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(width=100, height=100, bgcolor=ft.colors.PINK_200),
                                ft.Container(width=100, height=100, bgcolor=ft.colors.PINK_200),
                                ft.Container(width=100, height=100, bgcolor=ft.colors.PINK_200),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        bgcolor=ft.colors.RED,
                        alignment=ft.alignment.top_center
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(width=100, height=100, bgcolor=ft.colors.PINK_200),
                                ft.Container(width=100, height=100, bgcolor=ft.colors.PINK_200),
                                ft.Container(width=100, height=100, bgcolor=ft.colors.PINK_200),
                                ft.Container(width=100, height=100, bgcolor=ft.colors.PINK_200),
                                ft.Container(width=100, height=100, bgcolor=ft.colors.PINK_200),
                                ft.Container(width=100, height=100, bgcolor=ft.colors.PINK_200),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        bgcolor=ft.colors.LIME,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,


            ),
            bgcolor=ft.colors.CYAN_700,
            alignment=ft.alignment.center,
        )
    )

ft.app(target=main)