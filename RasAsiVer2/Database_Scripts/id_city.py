import psycopg2


def id_city(place, upass):
    place = place.capitalize()

    conn = psycopg2.connect(database='postgres', user='postgres', password=upass)
    cur = conn.cursor()

    cur.execute("""SELECT id_city FROM my_city WHERE (city=%s)""", (place,)) # TODO переписать my_city
    id_city = cur.fetchone()

    if not id_city:
        cur.execute("""INSERT INTO my_city (country, city) VALUES (%s, %s) RETURNING id_city""", ('some place', place))
        id_city = cur.fetchone()[0]
        conn.commit()
    else:
        id_city = id_city[0]

    cur.close()
    conn.close()

    return id_city

