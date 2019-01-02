from .config import config
import mysql.connector
print('print from __q2__')


def query_select(zapros, *argument2):
    print(f'запрос:\n{zapros}\nаргументы: {argument2}')
    connection1 = mysql.connector.connect(**config)

    cursor = connection1.cursor()

    cursor.execute(zapros, argument2)

    ok = cursor.fetchall()

    cursor.close()
    connection1.close()

    return ok
