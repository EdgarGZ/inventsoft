# Django
from django.urls import path


# Viewa
from apps.usuarios.views import login_user
from apps.usuarios.views import render_login
from apps.usuarios.views import table
from apps.usuarios.views import logout
from apps.usuarios.views import dashboard
from apps.usuarios.views import fetch_user
from apps.usuarios.views import stock
from apps.usuarios.views import sales
from apps.usuarios.views import purchases
from apps.usuarios.views import products
from apps.usuarios.views import fetch_products
from apps.usuarios.views import staff
from apps.usuarios.views import records
from apps.usuarios.views import notifications
from apps.usuarios.views import form
from apps.usuarios.views import fetch_categories_and_providers
from apps.usuarios.views import post_product
# from apps.usuarios.views import form_area
# from apps.usuarios.views import form_producot
# from apps.usuarios.views import form_staff

# URLPatterns
app_name='usuarios'
urlpatterns = [
    path('', render_login, name='render_login'),
    path('login/', login_user, name='login'),
    path('get_user/', fetch_user, name='get_user'),
    path('table/', table, name='table'),
    path('form/<slug:type>/', form, name='form'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
    path('stock/', stock, name='stock'),
    path('sales/', sales, name='sales'),
    path('purchases/', purchases, name='purchases'),
    
    # Products
    path('products/', products, name='products'),
    path('fetch_products/', fetch_products, name='get_products'),
    path('staff/', staff, name='staff'),
    path('records/', records, name='records'),
    path('notifications/', notifications, name='notifications'),
    path('categories_and_providers/', fetch_categories_and_providers, name='fetch_categories_and_providers'),
    path('post_product/', post_product, name='post_product'),
    # path('form_area/', form_area, name='form_area'),
    # path('form_product/', form_product, name='form_product'),
    # path('form_area/', form_area, name='form_area'),
]