import datetime

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView

from manager.forms import CustomUserRegisterForm, ChangeUserDetailForm
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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.age = datetime.date.today().year - self.object.birthday.year
        if self.object.birthday.month >= datetime.date.today().month:
            if self.object.birthday.day > datetime.date.today().day:
                self.object.age -= 1
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ChangeProfile(UpdateView):
    model = CustomUser
    template_name = 'change_user_page.html'
    form_class = ChangeUserDetailForm
    success_url = reverse_lazy("manager:start_page")


class ManagersView(View):
    def get(self, request):
        managers = CustomUser.objects.filter(is_staff=True)
        context = {"users": managers, "header": "Наши менеджеры:"}
        return render(request, 'list_users_page.html', context)


class TeachersView(View):
    def get(self, request):
        teachers = CustomUser.objects.filter(is_teacher=True)
        context = {"users": teachers, "header": "Наши преподователи:"}
        return render(request, 'list_users_page.html', context)


class StudentsView(View):
    def get(self, request):
        students = CustomUser.objects.filter(is_student=True)
        context = {"users": students, "header": "Наши студенты:"}
        return render(request, 'list_users_page.html', context)
