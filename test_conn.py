from connect_sql import *

conn = connect_sql('root', 'ThePassword', 'localhost', 'db_trabalho1')
print(conn.is_connected())