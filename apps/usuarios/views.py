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
from apps.usuarios.authentication import authenticate, get_user, login

# Query
from apps.usuarios.querys import execute_query, call_stored_procedure, call_view, fetch_area_user


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
                login(request, user=user)
                data = {
                    'response': user, 
                    'status': 200
                }
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
    resp = get_user(user_id=f'{user["emp_key"]}')
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
def fetch_product(request,id):
    
    data, product, view_name = {}, [], f'{id}VIEW'

    resp = call_view(f'CREATE OR REPLACE VIEW {view_name} AS SELECT Product.product_key, Product.name, Product.description, Product.price, Product.category, Product.provider, Stock.amount FROM Product, Stock WHERE Product.product_key = \'{id}\' AND Stock.product = \'{id}\';')
    if resp:
        resp = execute_query(f'SELECT * FROM {view_name}', 'one')
        if resp:
            product_list = resp[1]
            column_names = resp[0]
            product = {column:product_list[i] for i, column in enumerate(column_names)}
            data['product'] = product
        
    return JsonResponse(data)


@login_required
def fetch_product_stock(request, id):
    data, stock = {}, []

    resp = execute_query(f'SELECT * FROM Stock WHERE product = \'{id}\';', 'one')
    if resp:
        stock_list = resp[1]
        column_names = resp[0]
        stock = {column:stock_list[i] for i, column in enumerate(column_names)}
        data['stock'] = stock

    return JsonResponse(data)


@login_required
def fetch_provider(request, id):
    data, provider = {}, []

    resp = execute_query(f'SELECT * FROM Provider WHERE provider_key = \'{id}\';', 'one')
    if resp:
        provider_list = resp[1]
        column_names = resp[0]
        provider = {column:provider_list[i] for i, column in enumerate(column_names)}
        data['provider'] = provider

    return JsonResponse(data)


@login_required
def fetch_products(request):
    """
        fetch_products function retrieves all products in the D.B.
        and sends them to the front in JSON format
    """
    data, products = {}, []

    resp = execute_query('SELECT product_key as key, name, description, price, category, provider FROM Product ORDER BY product_key ASC;', 'all')
    if resp:
        product_list = resp[1]
        column_names = resp[0]
        products = [{column:row[i] for i, column in enumerate(column_names)} for row in product_list]
        data['products'] = products

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
        accion = request.POST['accion']
        if 'id' in request.POST:
                idProduct = request.POST['id']
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
            if accion == 'NEW':
                resp = call_stored_procedure(f'SELECT addProduct(\'{nombre}\', \'{descripcion}\', {float(precio)}, \'{categoria}\', \'{proveedor}\', {int(cantidad)})', 'one')
                if resp[1]:
                    data['status'] = 200
                    return JsonResponse(data)
                else:
                    data['status'] = 400
                    return JsonResponse(data)
            elif accion == 'EDIT':
                print(idProduct)
                resp = call_stored_procedure(f'SELECT editProduct(\'{idProduct}\',\'{nombre}\', \'{descripcion}\', {float(precio)}, \'{categoria}\', \'{proveedor}\', {int(cantidad)})', 'one')
                if resp[1]:
                    data['status'] = 200
                    return JsonResponse(data)
                else:
                    data['status'] = 400
                    return JsonResponse(data)


@login_required
def delete_product(request, id):
    data = {}
    resp = call_stored_procedure(f'SELECT deleteProduct(\'{id}\')', 'one')
    if resp[1]:
        data['status'] = 200
        return JsonResponse(data)
    else:
        data['status'] = 400
        return JsonResponse(data)


@login_required
def fetch_clients(request):
    data, clients = {}, []

    resp = execute_query('SELECT client_key as key, name, rfc, address, email, phone FROM Client', 'all')
    if resp:
        client_list = resp[1]
        column_names = resp[0]
        clients = [{column:row[i] for i, column in enumerate(column_names)} for row in client_list]
        data['clients'] = clients

    return JsonResponse(data)


@login_required
def fetch_sellers(request):
    data, sellers = {}, []

    resp = fetch_area_user(area_code='AV', user_type='employee', action='user', command='all')
    if resp:
        sellers_list = resp[1]
        column_names = resp[0]
        sellers = [{column:row[i] for i, column in enumerate(column_names)} for row in sellers_list]
        for i in range(len(sellers)):
            sellers[i]['name'] = f'{sellers[i]["first_name"]} {sellers[i]["last_name"]}'
        data['sellers'] = sellers

    return JsonResponse(data)


@login_required
def fetch_buyers(request):
    data, buyers = {}, []

    resp = fetch_area_user(area_code='AC', user_type='employee', action='user', command='all')
    if resp:
        buyers_list = resp[1]
        column_names = resp[0]
        buyers = [{column:row[i] for i, column in enumerate(column_names)} for row in buyers_list]
        for i in range(len(buyers)):
            buyers[i]['name'] = f'{buyers[i]["first_name"]} {buyers[i]["last_name"]}'
        data['buyers'] = buyers

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
def logout(request):
    response = redirect('usuarios:render_login')
    del request.session['user']
    return response

@login_required
def stock(request):
    """
        Stock function retrieves the stock html
    """
    return render(request, 'stock.html')


@login_required
def fetch_stock(request):
    data, stock = {}, []
    
    resp = execute_query('SELECT Stock.id, Stock.product, Stock.amount, Product.name as product_name FROM Stock, Product WHERE Product.product_key = Stock.product ORDER BY id ASC;', 'all')
    if resp:
        stock_list = resp[1]
        column_names = resp[0]
        stock = [{column:row[i] for i, column in enumerate(column_names)} for row in stock_list]
        data['stock'] = stock

    return JsonResponse(data)


@login_required
def fetch_stock_product(request, id):
    data, stock = {}, []

    resp = execute_query(f'SELECT Stock.id, Stock.product, Stock.amount, Product.name as product_name FROM Stock, Product WHERE Stock.id = {int(id)} AND Product.product_key = Stock.product ORDER BY id ASC;', 'one')
    if resp:
        stock_list = resp[1]
        column_names = resp[0]
        stock = {column:stock_list[i] for i, column in enumerate(column_names)}
        data['stock'] = stock

    return JsonResponse(data)


@login_required
def edit_stock(request):
    data = {}
    if request.method == 'POST':
        producto = request.POST['producto']
        cantidad = request.POST['cantidad']
        regex_cantitdad = r'[0-9]{,10}'
        if not re.match(regex_cantitdad, cantidad):
            data['status'] = 400
            data['error_desc'] = 'Cantidad o Precio invalido'
            return JsonResponse(data)
        else:
            resp = call_stored_procedure(f'SELECT editStock(\'{producto}\', {int(cantidad)})', 'one')
            print(resp)
            if resp[1]:
                data['status'] = 200
                return JsonResponse(data)
            else:
                data['status'] = 400
                return JsonResponse(data)


@login_required
def sales(request):
    """
        Sales function retrieves the sales html
    """
    return render(request, 'sales.html')


@login_required
def fetch_sales(request, flag, user=None):
    data, sales = {}, []
    
    if int(flag) == 1:
        resp = execute_query('SELECT Sale.id, Sale.product, Sale.amount, Sale.client, Sale.total, Sale.seller, DATE(Sale.sale_date) as sale_date, Product.name as name_product, Client.name as client_name, Employee.first_name, Employee.last_name  FROM Sale, Product, Client, Employee WHERE Product.product_key = Sale.product AND Client.client_key = Sale.client AND Employee.emp_key = Sale.seller;', 'all')
        if resp:
            sales_list = resp[1]
            column_names = resp[0]
            sales = [{column:row[i] for i, column in enumerate(column_names)} for row in sales_list]
            data['sales'] = sales
    elif int(flag) == 2:
        print(user)
        resp = execute_query(f'SELECT Sale.id, Sale.product, Sale.amount, Sale.client, Sale.total, Sale.seller, DATE(Sale.sale_date) as sale_date, Product.name as name_product, Client.name as client_name, Employee.first_name, Employee.last_name  FROM Sale, Product, Client, Employee WHERE Sale.seller = \'{user}\' AND Product.product_key = Sale.product AND Client.client_key = Sale.client AND Employee.emp_key = Sale.seller;', 'all')
        print(resp)
        if resp:
            sales_list = resp[1]
            column_names = resp[0]
            sales = [{column:row[i] for i, column in enumerate(column_names)} for row in sales_list]
            data['sales'] = sales

    return JsonResponse(data)


@login_required
def sell_product(request):
    data = {}
    if request.method == 'POST':
        product = request.POST['product']
        amount = request.POST['amount']
        total = request.POST['total']
        client = request.POST['client']
        employee = request.POST['employee']
        regex_precio = r'[0-9.]{,10}'
        regex_cantitdad = r'[0-9]{,10}'
        if not re.match(regex_precio, total) or not re.match(regex_cantitdad, amount):
            data['status'] = 400
            data['error_desc'] = 'Cantidad o Precio invalido'
            return JsonResponse(data)
        else:
            resp = call_stored_procedure(f'SELECT sellProduct(\'{product}\', {int(amount)}, \'{client}\', {float(total)}, \'{employee}\');', 'one')
            if resp[1]:
                data['status'] = 200
                return JsonResponse(data)
            else:
                data['status'] = 400
                return JsonResponse(data)


@login_required
def fetch_purchases(request, flag, user=None):
    data, purchases = {}, []

    if int(flag) == 1:
        resp = execute_query('SELECT Purchase.id, Purchase.product, Purchase.amount, Purchase.provider, Purchase.total, Purchase.buyer, DATE(Purchase.purchase_date) as purchase_date, Product.name as product_name, Provider.name as provider_name, Employee.first_name, Employee.last_name  FROM Purchase, Product, Provider, Employee WHERE Product.product_key = Purchase.product AND Provider.provider_key = Purchase.provider AND Employee.emp_key = Purchase.buyer;', 'all')
        if resp:
            sales_list = resp[1]
            column_names = resp[0]
            sales = [{column:row[i] for i, column in enumerate(column_names)} for row in sales_list]
            data['sales'] = sales
    elif int(flag) == 2:
        resp = execute_query(f'SELECT Purchase.id, Purchase.product, Purchase.amount, Purchase.provider, Purchase.total, Purchase.buyer, DATE(Purchase.purchase_date) as purchase_date, Product.name as name_product, Client.name as client_name, Employee.first_name, Employee.last_name  FROM Purchase, Product, Client, Employee WHERE Purchase.buyer = \'{user}\' AND Product.product_key = Purchase.product AND Client.client_key = Purchase.provider', 'all')
        if resp:
            sales_list = resp[1]
            column_names = resp[0]
            sales = [{column:row[i] for i, column in enumerate(column_names)} for row in sales_list]
            data['sales'] = sales

    return JsonResponse(data)


@login_required
def buy_product(request):
    data = {}
    if request.method == 'POST':
        product = request.POST['product']
        amount = request.POST['amount']
        total = request.POST['total']
        provider = request.POST['provider']
        employee = request.POST['employee']
        regex_precio = r'[0-9.]{,10}'
        regex_cantitdad = r'[0-9]{,10}'
        if not re.match(regex_precio, total) or not re.match(regex_cantitdad, amount):
            print('no')
            data['status'] = 400
            data['error_desc'] = 'Cantidad o Precio invalido'
            return JsonResponse(data)
        else:
            resp = call_stored_procedure(f'SELECT purchaseProduct(\'{product}\', {int(amount)}, \'{provider}\', {float(total)}, \'{employee}\');', 'one')
            print(resp)            
            if resp[1]:
                data['status'] = 200
                return JsonResponse(data)
            else:
                data['status'] = 400
                return JsonResponse(data)


@login_required
def delete_sale(request, id):
    data = {}
    resp = call_stored_procedure(f'SELECT deleteSale(\'{id}\')', 'one')
    if resp[1]:
        data['status'] = 200
        return JsonResponse(data)
    else:
        data['status'] = 400
        return JsonResponse(data)


@login_required
def delete_purchase(request, id):
    data = {}
    resp = call_stored_procedure(f'SELECT deletePurchase(\'{id}\')', 'one')
    if resp[1]:
        data['status'] = 200
        return JsonResponse(data)
    else:
        data['status'] = 400
        return JsonResponse(data)


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
    #     return JsonResponse(data)