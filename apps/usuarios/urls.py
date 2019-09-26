# Django
from django.urls import path


# Viewa
from apps.usuarios.views import login_user
from apps.usuarios.views import render_login
from apps.usuarios.views import table
from apps.usuarios.views import logout
from apps.usuarios.views import dashboard
from apps.usuarios.views import form

# URLPatterns
app_name='usuarios'
urlpatterns = [
    path('', render_login, name='render_login'),
    path('login/', login_user, name='login'),
    path('table/', table, name='table'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('form/', form, name='form'),
]