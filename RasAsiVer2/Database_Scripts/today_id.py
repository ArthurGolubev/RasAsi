import datetime
import psycopg2


def today_id(upass):
    """

    :param upass: Пароль от БД
    :return: id текущего дня
    """
    conn = psycopg2.connect(database='postgres', user='postgres', password=upass, host='localhost')
    cur = conn.cursor()

    cur.execute("""SELECT id_date_day FROM date_day WHERE ("date_day" = current_date)""")
    today_id = cur.fetchone()[0]

    if not today_id:
        cur.execute("""INSERT INTO "date_day" (date_day) VALUES (%s) RETURNING id_date_day""",
                    (datetime.datetime.today().date(), ))
        today_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()

    return today_id


if __name__ == '__main__':
    print(today_id(''))  # TODO Удалить

