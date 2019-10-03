from inventsoft.connections_pool import threaded_postgreSQL_pool

def execute_query(query=None, command=None):
    if query and command:
        try:
            tcp = threaded_postgreSQL_pool
            connection = tcp.getconn()
            cursor = connection.cursor()
            cursor.execute(query)
            if command.lower() == 'all':
                query_list = cursor.fetchall()
            elif command.lower() == 'one':
                query_list = cursor.fetchone()
            column_names = [desc[0] for desc in cursor.description]
            data = [column_names, list(query_list)]
            return data
        except Exception as e:
            return None
        finally:
            if (tcp):
                tcp.putconn(connection)
                print("Threaded PostgreSQL connection pool is closed")

    return None


def call_stored_procedure(query=None, command=None):
    if query and command:
        try:
            tcp = threaded_postgreSQL_pool
            connection = tcp.getconn()
            cursor = connection.cursor()
            cursor.execute(query)
            if command.lower() == 'one':
                query_list = cursor.fetchone()
            # elif command.lower() == 'all':
            #     query_list = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            data = [column_names, list(query_list)]
            connection.commit()
            return data
        except Exception as e:
            return None
        finally:
            if (tcp):
                tcp.putconn(connection)
                print("Threaded PostgreSQL connection pool is closed")

    return None


def call_view(query=None):
    try:
        tcp = threaded_postgreSQL_pool
        connection = tcp.getconn()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return True
    except Exception as e:
        return False
    finally:
        if (tcp):
            tcp.putconn(connection)
            print("Threaded PostgreSQL connection pool is closed")