from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('Login/', views.Login_view, name="Login"),
    path('Logout/', views.Logout_view, name="Logout"),
]
