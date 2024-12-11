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
            page=page
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