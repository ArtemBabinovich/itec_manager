from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = "start_page.html"


class CustomLogoutView(LogoutView):
    pass
