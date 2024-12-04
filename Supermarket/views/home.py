from controls.controls import (
    ft,
    Appbar,
    ProductCard,
    ProductData,
    Button
)
from random import randrange
import os

class Home(ft.View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.appbar = Appbar(
            page=page,
            actions=self.appbar_actions()
        )
        self.route = '/'
        self.padding = ft.padding.only(
            top=4,
            left=10,
            right=10,
            bottom=8
        )
        self.controls = [
            ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[
                            ProductCard(
                                page=page,
                                data=product
                            ) for product in self.load_products()
                        ]
                    )
                ],
                height=(self.page.height - 40) * 0.97,
                scroll=ft.ScrollMode.ADAPTIVE
            )
        ]
    
    def load_products(self):
        products: list[str] = os.listdir('assets/products')
        product_descriptions: list[ProductData] = []

        for product in products:
            product_descriptions.append(
                ProductData(
                    name= product.split('.')[0].capitalize(),
                    description= 'A very nice product for your life...',
                    price= randrange(100, 999),
                    image= f'/products/{product}'
                )
            )
        
        return product_descriptions
    
    def appbar_actions(self):
        if not self.page.data:
            actions: list[ft.Control] = [
                ft.Container(
                    content=Button(
                        page=self.page,
                        text='Login',
                        bgcolor=None,
                        on_click=lambda _: self.page.go('/login')
                    ),
                    padding=ft.padding.only(
                        right=10
                    )
                )
            ]
        
        else:
            actions: list[ft.Control] = [
                ft.Container(
                    content=Button(
                        page=self.page,
                        text=self.page.data['user'][0].upper(),
                        bgcolor=ft.Colors.with_opacity(0.05, 'black'),
                        height=35,
                        border_radius=35,
                        width=35,
                        alignment=ft.MainAxisAlignment.CENTER,
                        on_click=self.show_options
                    ),
                    padding=ft.padding.only(
                        right=10
                    )
                )
            ]
        
        return actions

    def show_options(self, e: ft.ControlEvent):
        user_options = UserOptions(page=self.page)
        displayed = False

        for control in self.page.overlay:
            if type(user_options) == type(control):
                self.page.overlay.remove(control)
                displayed = True

                break
        
        if not displayed:
            self.page.overlay.append(user_options)
        
        e.page.update()
        

class UserOptions(ft.Container):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.width = 250
        self.top = 4
        self.right = 8
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = 8
        self.content = ft.Column(
            controls=[
                Button(
                    page=page,
                    icon=ft.Icons.SHOPPING_CART,
                    color=ft.Colors.with_opacity(0.70, 'black'),
                    text='Carinho',
                    on_hover=self.hover,
                    padding=ft.padding.only(
                        left=8
                    ),
                    bgcolor=None
                ),
                Button(
                    page=page,
                    icon=ft.Icons.NOTIFICATIONS,
                    color=ft.Colors.with_opacity(0.70, 'black'),
                    text='Notificações',
                    on_hover=self.hover,
                    padding=ft.padding.only(
                        left=8
                    ),
                    bgcolor=None
                ),
                Button(
                    page=page,
                    icon=ft.Icons.SETTINGS,
                    color=ft.Colors.with_opacity(0.70, 'black'),
                    text='Configurações',
                    on_hover=self.hover,
                    padding=ft.padding.only(
                        left=8
                    ),
                    bgcolor=None
                ),
                Button(
                    page=page,
                    icon=ft.Icons.LOGOUT,
                    color=ft.Colors.with_opacity(0.70, 'black'),
                    text='Sair',
                    on_hover=self.hover,
                    padding=ft.padding.only(
                        left=8
                    ),
                    bgcolor=None
                )
            ],
            spacing=2
        )
    
    def hover(self, e: ft.HoverEvent):
        if e.data == 'true':
            e.control.bgcolor = ft.Colors.BLUE
        
        else:
            e.control.bgcolor = None
        
        e.page.update()