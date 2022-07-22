import mysql.connector

def connect_sql(user: str, password: str, host: str, database: str):
    connection = mysql.connector.connect(
                                user,
                                password,
                                host,
                                database='employees',
                                use_pure=False)

    return connection