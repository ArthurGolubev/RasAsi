import psycopg2
from psycopg2.extras import execute_values


def append_today_weather(upass, values):

    """

    :param upass: Пароль для входа в БД
    :param values: [(1, 1, datetime.datetime(2019, 7, 13, 23, 46, 34, 360336), 4, 0.2, 32, 90, 10, 1017, 768), (...)]
    :return: Nothing
    """

    conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=upass, host='localhost')
    cur = conn.cursor()

    execute_values(cur,
                   """INSERT INTO "weather_journal" (
                   id_place, time, Wind_mps, Precipitation_mm, Temperature_c, Cloudiness_percent, 
                   Humidity_percent, Atmosphere_pressure_hpa, Atmosphere_pressure_mmhg
                   ) VALUES %s""",
                   values)

    conn.commit()
    cur.close()
    conn.close()
    print('weather successfully added to database ☁😊')
