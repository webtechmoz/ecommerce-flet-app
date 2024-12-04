from views.home import ft, Home
from views.login import Login
from views.register import Register


def main(page: ft.Page):
    page.title = 'Supermercado'
    page.route = '/'

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
        
        page.update()
    
    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='assets', upload_dir='assets/uploads')
    