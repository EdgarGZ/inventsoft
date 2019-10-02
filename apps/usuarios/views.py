# Django
from django.shortcuts import render, redirect
from django.http import JsonResponse


# Decorators
from apps.usuarios.decorators import login_required


# Utilities
import psycopg2
import re


# Conections
from inventsoft.connections_pool import threaded_postgreSQL_pool


# Auth
from apps.usuarios.authentication import authenticate, get_user

# Query
from apps.usuarios.querys import execute_query, call_stored_procedure


# Views
def render_login(request):
    """
        Render login function retrieves the login html
    """
    return render(request, 'login.html')


def login_user(request):
    """
        Login user do the login functionality by getting all the data by
        the http verb POST.
        We do some validations before to avoid errors.
    """
    if request.method == 'POST':
        data = {
            'response': '', 
            'status': 400
        }
        response = JsonResponse(data)
        username = request.POST['username']
        password = request.POST['password']
        regex_email = r'[a-z0-9._%+-]+@[a-z0-9.-]+[\\.][a-z]{2,}$'
        regex_pass = r'[a-z0-9._%+-@=?¿]'
        if re.match(regex_email, username) and re.match(regex_pass, password):
            user = authenticate(username=username, password=password)
            if user:
                data = {
                    'response': user, 
                    'status': 200
                }
                request.session['user'] = user
                return JsonResponse(data)
            else:
                return response
        else:
            return response


@login_required
def fetch_user(request):
    """
    fetch_user function to retrieve te current logged in user
    """
    user = request.session['user']
    resp = get_user(user_id=f'\'{user["emp_key"]}\'')
    print(resp)
    data = {
        'user': resp
    }
    return JsonResponse(data)


@login_required
def dashboard(request):
    """
        Dashboard function retrieves the dashboard html
    """
    return render(request, 'dashboard.html')


@login_required
def products(request):
    """
        Products function retrieves the products html
    """
    return render(request, 'products.html')


@login_required
def fetch_products(request):
    """
        fetch_products function retrieves all products in the D.B.
        and sends them to the front in JSON format
    """
    data, products = {}, []

    resp = execute_query('SELECT * FROM Product', 'all')
    if resp:
        product_list = resp[1]
        column_names = resp[0]
        products = [{column:row[i] for i, column in enumerate(column_names)} for row in product_list]
        data['products'] = products

    return JsonResponse(data)

@login_required
def table(request):
    """
        Table function retrieves the table html
    """
    return render(request, 'table.html')

@login_required
def form(request, type):
    """
        Form function retrieves the form html
    """
    return render(request, 'form.html')


@login_required
def fetch_categories_and_providers(request):
    """
        fetch_areas function retrieves all products in the D.B.
        and sends them to the front in JSON format
    """
    data, categories, providers = {}, [], []

    resp = execute_query('SELECT category_key as key, name FROM Category', 'all')
    if resp:
        categories_list = resp[1]
        column_names = resp[0]
        categories = [{column:row[i] for i, column in enumerate(column_names)} for row in categories_list]

    resp = execute_query('SELECT provider_key as key, name FROM Provider', 'all')
    if resp:
        providers_list = resp[1]
        column_names = resp[0]
        providers = [{column:row[i] for i, column in enumerate(column_names)} for row in providers_list]

    data['categories'] = categories
    data['providers'] = providers
    return JsonResponse(data)


@login_required
def post_product(request):
    data = {}
    categorias = ['BOMBON', 'CHOCOLATE', 'CARAMELO', 'GALLETA', 'GOMITA', 'PALETA', 'PAPA']
    proveedores = ['DLAROSA', 'RIKOLINO', 'WONKA', 'JOLLYRAN', 'GABI', 'MARINELA', 'GAMESA', 'CORONADO', 'SABRITAS', 'COYOTES']
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria = request.POST['categoria']
        proveedor = request.POST['proveedor']
        cantidad = request.POST['cantidad']
        regex_precio = r'[0-9.]{,10}'
        regex_cantitdad = r'[0-9]{,10}'
        if not categoria in categorias or not proveedor in proveedores:
            data['status'] = 400
            data['error_desc'] = 'Categoria o Proveedor incorrectos'
            return JsonResponse(data)
        elif not re.match(regex_precio, precio) or not re.match(regex_cantitdad, cantidad):
            data['status'] = 400
            data['error_desc'] = 'Cantidad o Precio invalido'
            return JsonResponse(data)
        else:
            resp = call_stored_procedure(f'SELECT addProduct(\'{nombre}\', \'{descripcion}\', {float(precio)}, \'{categoria}\', \'{proveedor}\', {int(cantidad)})', 'one')
            if resp[1]:
                data['status'] = 200
                return JsonResponse(data)
            else:
                data['status'] = 400
                return JsonResponse(data)



@login_required
def logout(request):
    response = redirect('usuarios:render_login')
    response.delete_cookie('user')
    return response

@login_required
def stock(request):
    """
        Stock function retrieves the stock html
    """
    return render(request, 'stock.html')


@login_required
def sales(request):
    """
        Sales function retrieves the sales html
    """
    return render(request, 'sales.html')


@login_required
def purchases(request):
    """
        Purchases function retrieves the purchases html
    """
    return render(request, 'purchases.html')


@login_required
def staff(request):
    """
        Staff function retrieves the staff html
    """
    return render(request, 'staff.html')


@login_required
def records(request):
    """
        Records function retrieves the records html
    """
    return render(request, 'records.html')


@login_required
def notifications(request):
    """
        Notifications function retrieves the notifications html
    """
    return render(request, 'notifications.html')



    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = None

    #     try:
    #         tcp = threaded_postgreSQL_pool
            # connection = tcp.getconn()
            # cursor = connection.cursor()
            # query = f'SELECT username, email FROM auth_user WHERE username = \'{username}\''
            # cursor.execute_query(query)
            # user = cursor.fetchone()
            # column_names = [desc[0] for desc in cursor.description]
            # user = [value for value in user]
            # user = zip(column_names, user)
            # user_object = dict(user)
            # print(user_object)
    #     except (Exception, psycopg2.DatabaseError) as error :
    #         print ("Error while connecting to PostgreSQL", error)
    #     finally:
    #         if (tcp):
    #             tcp.putconn(connection)
    #             print("Threaded PostgreSQL connection pool is closed")

    #     data = {
    #         'response': user_object,
    #         'status': 200
    #     }
    #     return JsonResponse(data)