class BaseView:
    def render(self):
        print("Template render")

class LoggingMixin:
    def render(self):
        print("Log: start")
        super().render()
        print("Log: end")

class AuthRequiredMixin:
    def __init__(self, authed=True, **kwargs):
        self.authed = authed
        super().__init__(**kwargs)

    def render(self):
        if self.authed == True:
            print("Auth OK")
            super().render()
        else:
            print("Access denied")


class AdminPageView(LoggingMixin, AuthRequiredMixin, BaseView):
    def __init__(self, authed=True):
        super().__init__(authed=authed)

    def render(self):
        print("Admin page render start")
        super().render()
        print("Admin page render end")

# Тест:
admin_page = AdminPageView(authed=True)
admin_page.render()
