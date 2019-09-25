# Django
from django.shortcuts import render
from django.http import JsonResponse

# Utilities
import psycopg2
import re

# Conections
from inventsoft.connections_pool import threaded_postgreSQL_pool

# Auth
from apps.usuarios.authentication import authenticate

# Config
from inventsoft.common import config

def render_login(request):
    return render(request, 'login.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        regex_email = r'[a-z0-9._%+-]+@[a-z0-9.-]+[\\.][a-z]{2,}$'
        regex_pass = r'[a-z0-9._%+-@=?¿]+@[a-z0-9.-]+[\\.][a-z]{2,}$'
        if re.match(regex_email, username):
            user = authenticate(username=username, password=password)
            if user:
                config(user)
                print(config(user).getUser()['emp_key'])
                data = {
                    'response': user, 
                    'status': 200
                }
                return JsonResponse(data)
            else:
                data = {
                    'response': '', 
                    'status': 400
                }
                return JsonResponse(data)
    


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