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
                response = JsonResponse(data)
                response.set_cookie('user', user)
                return response
            else:
                response.set_cookie('user', user)
                return response
        else:
            response.set_cookie('user', user)
            return response

@login_required
def dashboard(request):
    """
        Dashboard function retrieves the dashboard html
    """
    return render(request, 'dashboard.html')

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
def fetch_user(request):
    cookie_user = request.COOKIES.get('user')
    list_user = cookie_user.split('\' :')
    user = str(list_user).split(':')
    uid = user[1].split(',')
    resp = get_user(user_id=uid[0])
    data = {
        'user': resp
    }
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
def products(request):
    """
        Products function retrieves the products html
    """
    return render(request, 'products.html')


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
            # cursor.execute(query)
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