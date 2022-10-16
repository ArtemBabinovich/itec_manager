from django.urls import path

from .views import CustomLoginView, CustomLogoutView

app_name = "manager"

urlpatterns = [
    path('', CustomLoginView.as_view(), name='start_page'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]