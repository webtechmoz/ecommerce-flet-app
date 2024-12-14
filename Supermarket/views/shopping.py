from controls.controls import (
    ft,
    Appbar,
    Button,
    ProductData,
    Text
)

class ShoppingCart(ft.View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.page.overlay.clear()
        self.appbar = Appbar(page=page)
        self.route = f'/{self.page.data['user']}/cart'
        self.controls = [
            ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[

                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )
        ]

        self.add_to_cart()
    
    def add_to_cart(self):
        keys = self.page.data.keys()

        # Adicionar o botão de pagamentos no appbar
        self.appbar.actions.append(
            ft.Container(
                content=Button(
                    page=self.page,
                    icon=ft.Icons.WALLET,
                    text=f'MT {format(0, ",.2f")}',
                    bgcolor=ft.Colors.with_opacity(0.08, 'black'),
                    padding=ft.padding.all(6),
                    alignment=ft.MainAxisAlignment.CENTER,
                    height=35,
                    border_radius=35,
                    icon_size=20,
                    on_click=lambda _: self.page.go(f'/{self.page.data['user']}/cart/checkout')
                ),
                padding=ft.padding.only(
                    right=6
                )
            )
        )

        self.appbar.actions[0], self.appbar.actions[1] = self.appbar.actions[1], self.appbar.actions[0]

        if 'products' in keys:
            products: list[ProductData] = self.page.data['products']

            if products:
                total = 0

                for product in products:
                    self.controls[0].controls[0].controls.append(
                        ProductCart(
                            page=self.page,
                            data=product
                        )
                    )

                    total += product.price
                
                self.appbar.actions[0].content.text_button.value = f'MT {format(total, ",.2f")}'
            
            else:
                self.controls[0].controls[0].controls.append(
                    ShoppingCartEmpty(
                        page=self.page
                    )
                )
        
        else:
            self.controls[0].controls[0].controls.append(
                ShoppingCartEmpty(
                    page=self.page
                )
            )

class ShoppingCartEmpty(ft.Column):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.col = {'xs': 6, 'sm': 4, 'md': 3}
        self.controls = [
            ft.Icon(
                name=ft.Icons.REMOVE_SHOPPING_CART_OUTLINED,
                color=ft.Colors.with_opacity(0.40, 'grey'),
                size=250
            ),
            Button(
                page=self.page,
                text='Explorar mais',
                alignment=ft.MainAxisAlignment.CENTER,
                on_click=lambda _: self.page.go('/')
            )
        ]
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

class ProductCart(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        data: ProductData
    ):
        super().__init__()
        self.page = page
        self.data = data
        self.bgcolor = ft.Colors.WHITE
        self.border_radius = 4
        self.padding = ft.padding.all(6)
        self.col = {'xs': 6, 'sm': 4, 'md': 3, 'lg': 2}
        self.content = ft.Column(
            controls=[
                ft.Container(
                    border_radius=4,
                    image=ft.DecorationImage(
                        src=self.data.image,
                        fit=ft.ImageFit.COVER
                    ),
                    height=200
                ),
                ft.Column(
                    controls=[
                        Text(
                            value=self.data.name,
                            color=ft.Colors.with_opacity(0.8, 'black'),
                            weight='bold'
                        ),
                        Text(
                            value=self.data.description,
                            color=ft.Colors.with_opacity(0.8, 'black')
                        )
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Row(
                                    controls=[
                                        Button(
                                            page=self.page,
                                            icon=ft.Icons.REMOVE,
                                            color=ft.Colors.with_opacity(0.8, 'white'),
                                            bgcolor=ft.Colors.with_opacity(0.5, 'grey'),
                                            width=22,
                                            height=22,
                                            border_radius=22,
                                            icon_size=14,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            on_click=self.remove_qtd
                                        ),
                                        Button(
                                            page=self.page,
                                            icon=ft.Icons.ADD,
                                            color=ft.Colors.with_opacity(0.8, 'white'),
                                            bgcolor=ft.Colors.with_opacity(0.5, 'blue'),
                                            width=22,
                                            height=22,
                                            border_radius=22,
                                            icon_size=14,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            on_click=self.add_qtd
                                        ),
                                        Button(
                                            page=self.page,
                                            icon=ft.Icons.DELETE,
                                            color=ft.Colors.with_opacity(0.8, 'white'),
                                            bgcolor=ft.Colors.with_opacity(0.5, 'red'),
                                            width=22,
                                            height=22,
                                            border_radius=22,
                                            icon_size=14,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            on_click=self.remove_to_cart
                                        )
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        text_qtd := Text(
                                            value='1',
                                            color=ft.Colors.with_opacity(0.8, 'black')
                                        ),
                                        text_price := Text(
                                            value=f'MT {format(self.data.price, ",.2f")}',
                                            color=ft.Colors.with_opacity(0.8, 'black')
                                        )
                                    ]
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ]
                )
            ]
        )

        self.text_qtd = text_qtd
        self.text_price = text_price
    
    def remove_to_cart(self, e: ft.ControlEvent):
        self.parent.controls.remove(self)
        self.page.data['products'].remove(self.data)

        self.total_price()

        if len(self.parent.controls) < 1:
            self.page.views[-1].controls[0].controls[0].controls.append(
                ShoppingCartEmpty(
                    page=self.page
                )
            )

        e.page.update()
    
    def add_qtd(self, e: ft.ControlEvent):
        qtd = int(self.text_qtd.value)

        self.text_qtd.value = qtd + 1
        self.text_price.value = f'MT {format(self.data.price * float(self.text_qtd.value), ",.2f")}'

        self.total_price()

        e.page.update()
    
    def remove_qtd(self, e: ft.ControlEvent):
        qtd = int(self.text_qtd.value)

        if qtd > 1:
            self.text_qtd.value = qtd - 1
            self.text_price.value = f'MT {format(self.data.price * float(self.text_qtd.value), ",.2f")}'

        self.total_price()

        e.page.update()
    
    def total_price(self):
        products: list[ProductCart] = self.parent.controls
        total = 0

        for product in products:
            total += int(product.text_qtd.value) * product.data.price
        
        self.page.views[-1].appbar.actions[0].content.text_button.value = f'MT {format(total, ",.2f")}'