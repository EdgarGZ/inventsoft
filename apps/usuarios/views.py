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
from apps.usuarios.authentication import authenticate


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
def home(request):
    """
        Home function retrieves the home html
    """
    return render(request, 'home.html')


@login_required
def logout(request):
    response = redirect('usuarios:render_login')
    response.delete_cookie('user')
    return response

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