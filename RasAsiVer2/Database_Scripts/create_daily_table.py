import psycopg2


def create_daily_table(upass):
    conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=upass, host='localhost')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS daily_ach (
    id_daily_ach serial PRIMARY KEY, 
    date date, 
    sp boolean NULL, 
    rs_ins boolean NULL, 
    read boolean NULL)""")

    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    create_daily_table(input('pass '))