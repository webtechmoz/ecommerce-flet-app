from views.home import ft, Home
from views.login import Login
from views.register import Register
from views.logout import LogOut
from views.shopping import ShoppingCart

def main(page: ft.Page):
    page.title = 'Supermercado'
    page.route = '/'
    page.data = {
        'user': 'azunguze'
    }

    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            android=ft.PageTransitionTheme.NONE,
            ios=ft.PageTransitionTheme.NONE,
            macos=ft.PageTransitionTheme.NONE,
            windows=ft.PageTransitionTheme.NONE,
            linux=ft.PageTransitionTheme.NONE
        )
    )

    def router(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(Home(page=page))
        
        elif page.route == '/login':
            page.views.append(Login(page=page))
        
        elif page.route == '/register':
            page.views.append(Register(page=page))
        
        elif page.route == '/logout':
            page.views.append(LogOut(page=page))
        
        elif '/cart' in page.route[-5::]:
            if page.data:
                if page.route == f'/{page.data['user']}/cart':
                    page.views.append(ShoppingCart(page=page))
                
                else:
                    page.go('/login')
            
            else:
                page.go('/login')
        
        page.update()
    
    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='assets', upload_dir='assets/uploads')
    