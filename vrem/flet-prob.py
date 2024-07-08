import flet as ft

def main(page: ft.Page):

    mgnvs_red = "#ab2524"
    mgnvs_ret_text = ft.TextStyle(color=mgnvs_red)
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    dd_departure = ft.Dropdown(
        label="Отправление",
        label_style=mgnvs_ret_text,
        border_color=mgnvs_red,
        options=[
            ft.dropdown.Option("LED"),
            ft.dropdown.Option("SVO"),
        ],
    )

    dd_direction = ft.Dropdown(
        label="Направление",
        label_style=mgnvs_ret_text,
        border_color=mgnvs_red,
        options=[
            ft.dropdown.Option("AER"),
            ft.dropdown.Option("GDX"),
            ft.dropdown.Option("OBV"),
        ],
    )
    dd_transfer = ft.Dropdown(
        label="Трансвер",
        label_style=mgnvs_ret_text,
        border_color=mgnvs_red,
        options=[
            ft.dropdown.Option("SVO"),
            ft.dropdown.Option("None STOP"),
        ],
    )
    dd_cargo_type = ft.Dropdown(
        label="Тип груза",
        label_style=mgnvs_ret_text,
        border_color=mgnvs_red,
        options=[
            ft.dropdown.Option("GENERAL"),
            ft.dropdown.Option("LIVE"),
            ft.dropdown.Option("FRESH"),
        ],
    )

    h_weight = ft.Text("Вход", size=50)
    h_res = ft.Text("Выход", size=50)

    in_res = 0
    out_res = 0

    txt_weight = ft.Text(str(in_res), size=30, color=mgnvs_red)
    txt_res = ft.Text(str(out_res), size=30, color=mgnvs_red)


    tf_fuel = ft.TextField(value="6", label="Топливо", hint_text="6", label_style=mgnvs_ret_text, border_color=mgnvs_red)
    tf_margin = ft.TextField(value="20", label="Маржа, %", label_style=mgnvs_ret_text, border_color=mgnvs_red)
    tf_num_places = ft.TextField(label="Кол-во мест, шт", label_style=mgnvs_ret_text, border_color=mgnvs_red)
    tf_weight = ft.TextField(label="Вес, кг", label_style=mgnvs_ret_text, border_color=mgnvs_red)
    tf_volume = ft.TextField(label="Объём, м³", label_style=mgnvs_ret_text, border_color=mgnvs_red)
    # def minus_click(e):
    #     txt_number.value = str(int(txt_number.value) - 1)
    #     page.update()
    #
    # def plus_click(e):
    #     txt_number.value = str(int(txt_number.value) + 1)
    #     page.update()

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.title = "Калькулятор"
    page.window_width = 700
    page.window_height = 620

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        tf_num_places,
                        tf_weight,
                        tf_volume,
                        ft.Divider(height=2, color="white"),
                        dd_departure,
                        dd_direction,
                        dd_transfer,
                        dd_cargo_type,
                        tf_fuel,
                        ft.Divider(height=2, color="white"),
                        tf_margin,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.VerticalDivider(width=2, color="white"),
                ft.Container(
                    content=ft.Column(
                    [
                            h_weight,
                            txt_weight,
                            h_res,
                            txt_res,
                        ],
                        height=545,
                        alignment=ft.MainAxisAlignment.START,


                    ),
                    alignment=ft.alignment.top_center,
                    # bgcolor=ft.colors.CYAN_700,
                    padding=0,
                    margin=0
                ),

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)