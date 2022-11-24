from django.contrib.admin import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('autoevaluaciones/', views.autoevaluaciones, name="Autoevaluaciones"),
    path('logout/', LogoutView.as_view(), name="LogOut"),
    path('login/', views.Login, name="LogIn"),
    path('registrar_caracterizacion/', views.caracterizacion, name="Registrar Caracterizacion" ),
]


