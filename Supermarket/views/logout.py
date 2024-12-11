from controls.controls import ft

class LogOut(ft.View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.page = page
        self.route = '/logout'
        self.page.data = None
        self.page.overlay.clear()
        self.page.go('/')