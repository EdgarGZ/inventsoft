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
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = None

        try:
            tcp = threaded_postgreSQL_pool
            connection = tcp.getconn()
            cursor = connection.cursor()
            query = f'SELECT * FROM auth_user WHERE username = \'{username}\''
            cursor.execute(query)
            user = cursor.fetchone()
            print(user)
        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            if (tcp):
                tcp.putconn(connection, close=True)
                print("Threaded PostgreSQL connection pool is closed")

        data = {
            'response': user,
            'status': 200
        }
        return JsonResponse(data)