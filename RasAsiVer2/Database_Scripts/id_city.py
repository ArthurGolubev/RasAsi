import psycopg2


def id_city(place, upass):
    place = place.capitalize()

    conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=upass, host='localhost')
    cur = conn.cursor()

    cur.execute("""SELECT id_place FROM my_place WHERE (place=%s)""", (place,))
    id_city = cur.fetchone()

    if not id_city:
        cur.execute("""INSERT INTO my_place (country, place) VALUES (%s, %s) RETURNING id_place""", ('some place', place))
        id_city = cur.fetchone()[0]
        conn.commit()
    else:
        id_city = id_city[0]

    cur.close()
    conn.close()

    return id_city

