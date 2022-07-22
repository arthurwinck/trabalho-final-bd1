import mysql.connector

def connect_sql(user: str, password: str, host: str, database: str):
    connection = mysql.connector.connect(
                                user=user,
                                password=password,
                                host=host,
                                database=database,
                                use_pure=False, auth_plugin='mysql_native_password')

    return connection


