from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
    path("",views.index,name="index"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("password_change/", views.change_password, name="password_change"),
    path("login_using_phone", views.login_using_phone, name="login_using_phone"),
]