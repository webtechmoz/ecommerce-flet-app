import flet as ft

class ProductData:
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        image: str
    ):
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        

class Text(ft.Text):
    def __init__(
        self,
        value: str,
        color: ft.Colors = ft.Colors.WHITE,
        size: int = 14,
        weight: ft.FontWeight = None,
        selectable: bool = True,
        text_align: ft.TextAlign = ft.TextAlign.START,
        no_wrap: bool = True
    ):
        super().__init__()
        self.value = value
        self.size = size
        self.color = color
        self.weight = weight
        self.selectable = selectable
        self.text_align = text_align
        self.no_wrap = no_wrap

class TextField(ft.TextField):
    def __init__(
        self,
        hint_text: str,
        color: ft.Colors = ft.Colors.BLACK,
        bgcolor: ft.Colors = ft.Colors.with_opacity(0.05, 'black'),
        border_radius: float = 2,
        border: ft.InputBorder = None,
        border_width: float = 1,
        border_color: ft.Colors = ft.Colors.with_opacity(0.05, 'black'),
        password: bool = False,
        icon: ft.Icons = None,
        autofocus: bool = False,
    ):
        super().__init__()
        self.hint_text = hint_text
        self.bgcolor = bgcolor
        self.autofocus = autofocus
        self.password = password
        self.prefix_icon = icon
        self.border_radius = border_radius
        self.border = border
        self.border_color = border_color
        self.border_width = border_width
        self.focused_bgcolor = self.bgcolor
        self.text_vertical_align = 0.40
        self.focused_border_color = self.border_color
        self.focused_border_width = border_width
        self.hint_style = ft.TextStyle(
            size=14,
            color=ft.Colors.with_opacity(0.3, color),
            weight='bold'
        )
        self.text_style = ft.TextStyle(
            size=14,
            color=ft.Colors.with_opacity(0.8, color),
            weight='bold'
        )

class Button(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        text: str = None,
        icon: ft.Icons = None,
        color: ft.Colors = ft.Colors.WHITE,
        bgcolor: ft.Colors = ft.Colors.BLUE,
        on_click: ft.ControlEvent = None,
        border_radius: float = 2,
        height: float = 40,
        width: float = None,
        col: dict[str, float] = {'xs': 12},
        alignment: ft.MainAxisAlignment = ft.MainAxisAlignment.START,
        on_hover: ft.HoverEvent = None,
        padding: ft.padding = None
    ):
        super().__init__()
        self.page = page
        self.col = col
        self.width = width
        self.padding = padding
        self.border_radius = border_radius
        self.height = height
        self.on_click = on_click
        self.on_hover = self.hover if not on_hover else on_hover
        self.bgcolor = bgcolor
        self.bcolor = bgcolor
        self.content = ft.Row(
            controls=[
                ft.Icon(
                    name=icon,
                    size=25 if icon else 0,
                    color=color
                ),
                Text(
                    value=text,
                    color=color,
                    selectable=False
                )
            ],
            spacing=2,
            alignment=alignment
        )
    
    def hover(self, e: ft.HoverEvent):
        if e.data == 'true':
            if self.bgcolor:
                self.bgcolor = ft.Colors.with_opacity(0.8, self.bcolor)
            
            self.content.controls[-1].weight = 'bold'
        
        else:
            self.bgcolor = self.bcolor
            self.content.controls[-1].weight = None
        
        self.page.update()

class ProductCard(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        data: ProductData
    ):
        super().__init__()
        self.page = page
        self.data = data
        self.col = {'xs': 6, 'sm': 4, 'md': 3, 'lg': 2}
        self.border_radius = 2
        self.bgcolor = ft.Colors.WHITE
        self.padding = ft.padding.all(4)
        self.content = ft.Stack(
            controls=[
                ft.Column(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Container(
                                    border_radius=2,
                                    image=ft.DecorationImage(
                                        src='no_product.jpg' if self.data.image == None else self.data.image,
                                        fit=ft.ImageFit.COVER,
                                        opacity=0.10 if self.data.image == None else 1
                                    ),
                                    height=150,
                                    bgcolor=ft.Colors.with_opacity(0.05, 'black')
                                ),
                                Text(
                                    value=self.data.name.capitalize(),
                                    color=ft.Colors.with_opacity(0.8, 'black'),
                                    no_wrap=False,
                                    text_align=ft.TextAlign.CENTER
                                )
                            ],
                            spacing=2,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                Text(
                                    value=f'MT {format(float(self.data.price), ",.2f")}',
                                    color=ft.Colors.BLUE,
                                    weight='bold'
                                ),
                                Button(
                                    page=page,
                                    icon=ft.Icons.SHOPPING_CART,
                                    color=ft.Colors.BLUE,
                                    bgcolor=None,
                                    on_click=lambda _: print(f'Comprar {self.data.name} por MT {self.data.price}')
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ]
                )
            ]
        )

class Appbar(ft.AppBar):
    def __init__(
        self,
        page: ft.Page,
        actions: list[ft.Control] = None
    ):
        super().__init__()
        self.page = page
        self.bgcolor = ft.Colors.BLUE
        self.toolbar_height = 40
        self.title = ft.Row(
            controls=[
                ft.Icon(
                    name=ft.Icons.SHOP,
                    color=ft.Colors.WHITE,
                    size=25
                ),
                Text(
                    value=self.page.title.upper(),
                    size=20,
                    weight='bold'
                )
            ],
            spacing=2
        )
        self.title_spacing = 4
        self.actions = actions