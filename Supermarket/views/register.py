from controls.controls import (
    ft,
    Button,
    Text,
    TextField
)

class Register(ft.View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.route = '/register'
        self.page = page
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    RegisterContainer(page=page)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]

class RegisterContainer(ft.Container):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.bgcolor = ft.Colors.WHITE
        self.col = {'xs': 11, 'sm': 8, 'md': 4, 'lg': 2.80}
        self.border_radius = 4
        self.shadow = ft.BoxShadow(
            spread_radius=3,
            blur_radius=3,
            color=ft.Colors.BLACK,
            offset=ft.Offset(x=0, y=0),
            blur_style=ft.ShadowBlurStyle.OUTER
        )
        self.padding = ft.padding.only(
            top=15,
            left=8,
            right=8,
            bottom=8
        )
        self.content = ft.Column(
            controls=[
                Text(
                    value='Create Account',
                    size=16,
                    weight='bold',
                    color=ft.Colors.with_opacity(0.8, 'black')
                ),
                ft.Column(
                    controls=[
                        TextField(
                            hint_text='Username',
                            icon=ft.Icons.PERSON,
                            autofocus=True
                        ),
                        TextField(
                            hint_text='Email',
                            icon=ft.Icons.EMAIL,
                        ),
                        TextField(
                            hint_text='Password',
                            icon=ft.Icons.KEY,
                            password=True
                        ),
                        TextField(
                            hint_text='Confirm password',
                            icon=ft.Icons.KEY,
                            password=True
                        )
                    ],
                    spacing=8
                ),
                ft.Column(
                    controls=[
                        ft.ResponsiveRow(
                            controls=[
                                Button(
                                    page=page,
                                    text='Register',
                                    bgcolor=ft.Colors.BLUE,
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                Button(
                                    page=page,
                                    text='I have an account',
                                    color=ft.Colors.with_opacity(0.5, 'black'),
                                    bgcolor=None,
                                    on_click=lambda _: page.go('/login')
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=0
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )