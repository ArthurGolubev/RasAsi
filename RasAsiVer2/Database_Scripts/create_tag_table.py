import psycopg2


def create_tag_table(upass):
    conn = psycopg2.connect(database='postgres', user='postgres', password=upass, host='localhost')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS tag_table (
    id_tag serial PRIMARY KEY,
    rid_storage integer NULL UNIQUE REFERENCES storage, 
    sql boolean NULL, 
    rs boolean NULL, 
    python boolean NULL, 
    other boolean NULL)""")  # TODO добавить референсы на другие таблицы попимо rid_storage

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    create_tag_table(upass=input('pass '))