from views.home import ft, Home

def main(page: ft.Page):
    page.title = 'Supermercado'

    home = Home(page=page)

    def router(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(home)
        
        page.update()
    
    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='assets', upload_dir='assets/uploads')
    