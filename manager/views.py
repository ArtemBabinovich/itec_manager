from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from manager.forms import CustomUserRegisterForm
from manager.models import CustomUser


class CustomLoginView(LoginView):
    template_name = "start_page.html"


class CustomLogoutView(LogoutView):
    pass


class RegisterCustomUserView(CreateView):
    model = CustomUser
    template_name = 'register_form.html'
    form_class = CustomUserRegisterForm
    success_url = reverse_lazy('manager:start_page')


class CustomDetailView(DetailView):
    model = CustomUser
    template_name = 'detail_user_page.html'
