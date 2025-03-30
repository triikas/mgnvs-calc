import flet as ft
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import asyncio

params = {}


async def connect():
    global params
    try:
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]

        credentials = ServiceAccountCredentials.from_json_keyfile_name("assets/calc-416509-5e45d4492f28.json", scopes)
        file = gspread.authorize(credentials)
        sheet = file.open("ВВЛ")
        worksheet2 = sheet.worksheet('Лист2')
        GENERAL = list(map(lambda x: int(x.value), worksheet2.range('I6:I43') + worksheet2.range('I46:I99')))
        LIVE = list(map(lambda x: int(x.value), worksheet2.range('M6:M43') + worksheet2.range('M46:M99')))
        FRESH = list(map(lambda x: int(x.value), worksheet2.range('P6:P43') + worksheet2.range('P46:P99')))
        EXPRESS = list(map(lambda x: int(x.value), worksheet2.range('J6:J43') + worksheet2.range('J46:J99')))
        COURIER = list(map(lambda x: int(x.value), worksheet2.range('K6:K43') + worksheet2.range('K46:K99')))
        SAFE_VAL = list(map(lambda x: int(x.value), worksheet2.range('L6:L43') + worksheet2.range('L46:L99')))
        SAFE_HUM = list(map(lambda x: int(x.value), worksheet2.range('N6:N43') + worksheet2.range('N46:N99')))
        BIG = list(map(lambda x: int(x.value), worksheet2.range('O6:O43') + worksheet2.range('O46:O99')))
        PHARMA = list(map(lambda x: int(x.value), worksheet2.range('Q6:Q43') + worksheet2.range('Q46:Q99')))
        DGR = list(map(lambda x: int(x.value), worksheet2.range('R6:R43') + worksheet2.range('R46:R99')))
        WHEELS = list(map(lambda x: int(x.value), worksheet2.range('S6:S43') + worksheet2.range('S46:S99')))
        VACCINES = list(map(lambda x: int(x.value), worksheet2.range('T6:T43') + worksheet2.range('T46:T99')))
        FROM = list(map(lambda x: x.value, worksheet2.range('C6:C43') + worksheet2.range('C46:C99')))
        TO = list(map(lambda x: x.value, worksheet2.range('D6:D43') + worksheet2.range('D46:D99')))
        TRANSFER = list(map(lambda x: x.value, worksheet2.range('E6:E43') + worksheet2.range('E46:E99')))
        for i in range(len(TRANSFER)):
            if TRANSFER[i] == '':
                TRANSFER[i] = "None STOP"

    except:
        params = -1
    else:

        params = {
            "GENERAL": GENERAL,
            "LIVE": LIVE,
            "FRESH": FRESH,
            "EXPRESS": EXPRESS,
            "COURIER": COURIER,
            "SAFE_VAL": SAFE_VAL,
            "SAFE_HUM": SAFE_HUM,
            "BIG": BIG,
            "PHARMA": PHARMA,
            "DGR": DGR,
            "WHEELS": WHEELS,
            "VACCINES": VACCINES,
            "FROM": FROM,
            "TO": TO,
            "TRANSFER": TRANSFER,
        }


async def main(page: ft.Page):
    awa = connect()
    mgnvs_red = "#ab2524"
    mgnvs_ret_text = ft.TextStyle(color=mgnvs_red)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    async def in_res(e):
        if params != -1:
            param_list = [dd_departure.value, dd_direction.value, dd_transfer.value, dd_cargo_type.value]
            t_num = ''
            if '' not in param_list and None not in param_list:
                for i in range(len(params["GENERAL"])):
                    # print([params["FROM"][i], params["TO"][i], params["TRANSFER"][i],params[dd_cargo_type.value.replace("/", "_")][i]])
                    if dd_departure.value == params["FROM"][i] and dd_direction.value == params["TO"][i] and dd_transfer.value == params["TRANSFER"][i]:
                        t_num = params[dd_cargo_type.value.replace("/", "_")][i]

                        break
            print(t_num)
            if tf_fuel.value == '' or tf_weight.value == '' or tf_volume.value == '' or tf_margin.value == '':
                txt_weight.value = "Нет данных"
                txt_res.value = "Нет данных"
            elif t_num == "":
                txt_weight.value = "Нет подходящих"
                txt_res.value = "Нет подходящих"
            else:
                res = (float(tf_fuel.value) + t_num) * max([25, float(tf_weight.value), 167 * float(tf_volume.value) ])
                txt_weight.value = str(round(res))
                txt_res.value = str(round(res * (int(tf_margin.value) + 100) / 100))
            page.update()

    async def set_to(e):
        if dd_direction.value != '':
            new_transfer = []
            new_from = []
            next = False
            for i in range(len(params["GENERAL"])):
                if params["TO"][i] == dd_direction.value:
                    new_transfer.append(params["TRANSFER"][i])
                    new_from.append(params["FROM"][i])
                    next = True
                elif next:
                    break
            print(new_from)
            dd_departure.options = list(map(lambda i: ft.dropdown.Option(i), new_from))
            dd_transfer.options = list(map(lambda i: ft.dropdown.Option(i), new_transfer))
            page.update()
        else:
            dd_departure.options = [
            ft.dropdown.Option("LED"),
            ft.dropdown.Option("KJA"),
            ft.dropdown.Option("None STOP"),
        ]
            dd_transfer.options = [
            ft.dropdown.Option("SVO"),
            ft.dropdown.Option("VKO / DME"),
        ]
            page.update()

    async def txt_connect(e):

        if h_connect.value != "Подключено":
            await connect()
            if params != -1:
                h_connect.value = "Подключено"
                h_connect.color = "#32CD32"
                page.update()

    dd_departure = ft.Dropdown(
        label="Отправление",
        label_style=mgnvs_ret_text,
        border_color=mgnvs_red,
        options=[
            ft.dropdown.Option("SVO"),
            ft.dropdown.Option("VKO / DME"),
        ],
        on_change=in_res,
    )
    dd_direction = ft.TextField(
        label="Направление",
        label_style=mgnvs_ret_text,
        border_color=mgnvs_red,
        hint_text="AAQ",
        on_change=in_res,
        on_blur=set_to
    )
    dd_transfer = ft.Dropdown(
        label="Трансфер",
        label_style=mgnvs_ret_text,
        border_color=mgnvs_red,
        options=[
            ft.dropdown.Option("LED"),
            ft.dropdown.Option("KJA"),
            ft.dropdown.Option("None STOP"),
        ],
        on_change=in_res,
    )
    dd_cargo_type = ft.Dropdown(
        label="Тип груза",
        label_style=mgnvs_ret_text,
        border_color=mgnvs_red,
        options=[
            ft.dropdown.Option("GENERAL"),
            ft.dropdown.Option("LIVE"),
            ft.dropdown.Option("FRESH"),
            ft.dropdown.Option("EXPRESS"),
            ft.dropdown.Option("COURIER"),
            ft.dropdown.Option("SAFE/VAL"),
            ft.dropdown.Option("SAFE/HUM"),
            ft.dropdown.Option("BIG"),
            ft.dropdown.Option("DGR"),
            ft.dropdown.Option("WHEELS"),
            ft.dropdown.Option("VACCINES"),
        ],
        on_change=in_res,
    )

    h_weight = ft.Text("Вход", size=40)
    h_res = ft.Text("Выход", size=40)
    h_connect = ft.Text("Не подключено", size=40, color=mgnvs_red)
    h_connect.value = "Подключено"
    h_connect.color = "#32CD32"

    txt_weight = ft.Text(str(0), size=30, color=mgnvs_red)
    txt_res = ft.Text(str(0), size=30, color=mgnvs_red)

    def foo(e, data):
        print(data)

    tf_fuel = ft.TextField(value="6", label="Топливо", hint_text="6", label_style=mgnvs_ret_text, border_color=mgnvs_red, on_change=in_res)#, on_focus=txt_connect)
    tf_margin = ft.TextField(value="20", label="Маржа, %", label_style=mgnvs_ret_text, border_color=mgnvs_red, on_change=in_res)#, on_focus=txt_connect)
    tf_num_places = ft.TextField(label="Кол-во мест, шт", label_style=mgnvs_ret_text, border_color=mgnvs_red, on_change=in_res)#, on_focus=txt_connect)
    tf_weight = ft.TextField(label="Вес, кг", label_style=mgnvs_ret_text, border_color=mgnvs_red, on_change=in_res)#, on_focus=txt_connect)
    tf_volume = ft.TextField(label="Объём, м³", label_style=mgnvs_ret_text, border_color=mgnvs_red, on_change=in_res, on_focus=lambda e: foo(e, "asd"))#, on_focus=txt_connect)

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.title = "Калькулятор"
    page.window.width = 700
    page.window.height = 620
    page.on_app_lifecycle_state_change=txt_connect

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        tf_num_places,
                        tf_weight,
                        tf_volume,
                        ft.Divider(height=2, color="white"),
                        dd_direction,
                        dd_departure,
                        dd_transfer,
                        dd_cargo_type,
                        tf_fuel,
                        ft.Divider(height=2, color="white"),
                        tf_margin,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.VerticalDivider(width=2, color="white"),
                    ft.Column(
                        [ft.Container(
                            content=ft.Column(
                                [
                                    h_weight,
                                    txt_weight,
                                    h_res,
                                    txt_res,
                                ],
                                height=445,
                                alignment=ft.MainAxisAlignment.START,

                            ),
                            alignment=ft.alignment.top_center,
                            padding=0,
                            margin=0
                        ),
                        h_connect,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )


            ],
            alignment=ft.MainAxisAlignment.CENTER,

        )
    )
    await awa
ft.app(target=main, assets_dir="assets")