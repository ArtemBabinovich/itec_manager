from django.urls import path

from .views import CustomLoginView, CustomLogoutView, RegisterCustomUserView, \
    CustomDetailView, ChangeProfile, ManagersView, TeachersView, StudentsView

app_name = "manager"

urlpatterns = [
    path('', CustomLoginView.as_view(), name='start_page'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register_user/', RegisterCustomUserView.as_view(), name='register_user'),
    path('managers/', ManagersView.as_view(), name='managers_page'),
    path('teachers/', TeachersView.as_view(), name='teachers_page'),
    path('students/', StudentsView.as_view(), name='students_page'),
    path('user/<int:pk>', CustomDetailView.as_view(), name='user_detail'),
    path('user/change/<int:pk>', ChangeProfile.as_view(), name='change_user_detail'),
]