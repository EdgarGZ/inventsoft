# Django
from django.urls import path

# Viewa
from apps.usuarios.views import login_user
from apps.usuarios.views import render_login

app_name='usuarios'
urlpatterns = [
    path('', render_login, name='render_login'),
    path('login/', login_user, name='login'),
]