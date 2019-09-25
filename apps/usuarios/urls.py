# Django
from django.urls import path


# Viewa
from apps.usuarios.views import login_user
from apps.usuarios.views import render_login
from apps.usuarios.views import home
from apps.usuarios.views import logout


# URLPatterns
app_name='usuarios'
urlpatterns = [
    path('', render_login, name='render_login'),
    path('login/', login_user, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout, name='logout'),
]