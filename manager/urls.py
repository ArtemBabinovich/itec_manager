from django.urls import path

from .views import CustomLoginView, CustomLogoutView, RegisterCustomUserView, CustomDetailView, ChangeProfile

app_name = "manager"

urlpatterns = [
    path('', CustomLoginView.as_view(), name='start_page'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register_user/', RegisterCustomUserView.as_view(), name='register_user'),
    path('user/<int:pk>', CustomDetailView.as_view(), name='user_detail'),
    path('user/change/<int:pk>', ChangeProfile.as_view(), name='change_user_detail'),
]