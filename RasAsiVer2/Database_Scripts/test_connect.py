import psycopg2


def test_connection(upass):
    conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=upass, host='localhost')
    conn.close()
    return 1


if __name__ == '__main__':
    test_connection(upass=input('pass '))