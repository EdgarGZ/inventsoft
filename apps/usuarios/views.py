# Django
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Utilidades
import psycopg2
from psycopg2 import pool

# Conections
from inventsoft.connections_pool import threaded_postgreSQL_pool

# Create your views here.
def render_template(render, request, template):
    return ("""
        {obj_render}({obj_request}, '{template_name}')
    """.format(
        obj_render = render,
        obj_request = request,
        template_name = template
    ))

def render_login(request):
    return render(request, 'login.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = None

        try:
            tcp = threaded_postgreSQL_pool
            connection = tcp.getconn()
            cursor = connection.cursor()
            query = f'SELECT username, email FROM auth_user WHERE username = \'{username}\''
            cursor.execute(query)
            user = cursor.fetchone()
            column_names = [desc[0] for desc in cursor.description]
            user = [value for value in user]
            user = zip(column_names, user)
            user_object = dict(user)
            print(user_object)
        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            if (tcp):
                tcp.putconn(connection, close=True)
                print("Threaded PostgreSQL connection pool is closed")

        data = {
            'response': user_object,
            'status': 200
        }
        return JsonResponse(data)