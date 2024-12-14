from controls.controls import (
    ft,
    Appbar,
    Text,
    TextField,
    Button
)

class CheckOut(ft.View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.appbar = Appbar(page=page)
        self.route = f'/{self.page.data['user']}/cart/checkout'
        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    PaymentInfo(
                        page=self.page
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.ResponsiveRow(
                controls=[
                    AdressInfo(
                        page=self.page
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.ResponsiveRow(
                controls=[
                    Button(
                        page=self.page,
                        text='Pagar',
                        alignment=ft.MainAxisAlignment.CENTER,
                        border_radius=6,
                        col={'xs': 12, 'sm': 10, 'md': 8}
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
        self.scroll = ft.ScrollMode.ADAPTIVE

class PaymentInfo(ft.Container):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = 6
        self.padding = ft.padding.all(8)
        self.col = {'xs': 12, 'sm': 10, 'md': 8}
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        Text(
                            value='Forma de Pagamento',
                            color=ft.Colors.with_opacity(0.8, 'black'),
                            size=16,
                            weight='bold'
                        ),
                        ft.Divider(
                            height=1,
                            thickness=1,
                            color=ft.Colors.with_opacity(0.2, 'grey')
                        )
                    ],
                    spacing=0
                ),
                ft.RadioGroup(
                    content=ft.Row(
                        controls=[
                            ft.Radio(
                                label='M-Pesa',
                                value='m_pesa'
                            ),
                            ft.Radio(
                                label='Credit Card',
                                value='credit_card'
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                )
            ]
        )

class AdressInfo(ft.Container):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = 6
        self.padding = ft.padding.all(8)
        self.col = {'xs': 12, 'sm': 10, 'md': 8}
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        Text(
                            value='Endereço de Entrega',
                            color=ft.Colors.with_opacity(0.8, 'black'),
                            size=16,
                            weight='bold'
                        ),
                        ft.Divider(
                            height=1,
                            thickness=1,
                            color=ft.Colors.with_opacity(0.2, 'grey')
                        )
                    ],
                    spacing=0
                ),
                ft.ResponsiveRow(
                    controls=[
                        TextField(
                            label='Primeiro Nome',
                            col={'xs': 12, 'sm': 6},
                            autofocus=True,
                            height=46,
                            border_radius=8,
                            bgcolor=ft.Colors.TRANSPARENT
                        ),
                        TextField(
                            label='Último Nome',
                            col={'xs': 12, 'sm': 6},
                            height=46,
                            border_radius=8,
                            bgcolor=ft.Colors.TRANSPARENT
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    controls=[
                        TextField(
                            label='País',
                            col={'xs': 12, 'sm': 6},
                            height=46,
                            border_radius=8,
                            bgcolor=ft.Colors.TRANSPARENT
                        ),
                        TextField(
                            label='Provincia',
                            col={'xs': 6, 'sm': 3},
                            height=46,
                            border_radius=8,
                            bgcolor=ft.Colors.TRANSPARENT
                        ),
                        TextField(
                            label='Cidade',
                            col={'xs': 6, 'sm': 3},
                            height=46,
                            border_radius=8,
                            bgcolor=ft.Colors.TRANSPARENT
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    controls=[
                        TextField(
                            label='Rua/Avenida',
                            col={'xs': 12, 'sm': 6},
                            height=46,
                            border_radius=8,
                            bgcolor=ft.Colors.TRANSPARENT
                        ),
                        TextField(
                            label='Número',
                            col={'xs': 6, 'sm': 3},
                            height=46,
                            border_radius=8,
                            bgcolor=ft.Colors.TRANSPARENT
                        ),
                        TextField(
                            label='CIP',
                            col={'xs': 6, 'sm': 3},
                            height=46,
                            border_radius=8,
                            bgcolor=ft.Colors.TRANSPARENT
                        )
                    ]
                )
            ]
        )
