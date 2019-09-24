# Django
from django.urls import path

# Viewa
from apps.usuarios.views import login_user

app_name='usuarios'
urlpatterns = [
    path('login/', login_user, name='login'),
]