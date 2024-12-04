from controls.controls import (
    ft,
    Button,
    Text,
    TextField
)

class Login(ft.View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.route = '/login'
        self.page = page
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    LoginContainer(page=page)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]

class LoginContainer(ft.Container):
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
                    value='Login',
                    size=16,
                    weight='bold',
                    color=ft.Colors.with_opacity(0.8, 'black')
                ),
                ft.Column(
                    controls=[
                        text_username := TextField(
                            hint_text='Username por Email',
                            icon=ft.Icons.PERSON,
                            autofocus=True
                        ),
                        text_password := TextField(
                            hint_text='Password',
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
                                    text='Login',
                                    bgcolor=ft.Colors.BLUE,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    on_click=self.login_event
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                Button(
                                    page=page,
                                    text='Recover password',
                                    color=ft.Colors.with_opacity(0.5, 'black'),
                                    bgcolor=None
                                ),
                                Button(
                                    page=page,
                                    text='Create account',
                                    color=ft.Colors.with_opacity(0.5, 'black'),
                                    bgcolor=None,
                                    on_click=lambda _: page.go('/register')
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ],
                    spacing=0
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )

        self.text_username = text_username
        self.text_password = text_password
    
    def login_event(self, e: ft.ControlEvent):
        if self.text_username.value and self.text_password.value:
            self.page.data = {
                'user': self.text_username.value
            }

            e.page.go('/')
        
        else:
            self.text_username.focus()

        self.text_username.value = ''
        self.text_password.value = ''

        e.page.update()
        
