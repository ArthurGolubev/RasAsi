import psycopg2
import datetime
import subprocess
from sys import platform
from psycopg2.extras import execute_values
from RasAsiVer2.Google.GoogleDrive import GoogleDrive


class RasAsiDatabase:

    def test_connection(self, upass):
        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=upass, host='localhost')
        conn.close()
        return 1

    def id_place(self, place, upass):
        place = place.capitalize()

        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""SELECT id_place FROM my_place WHERE (place=%s)""", (place,))
        id_place = cur.fetchone()

        if not id_place:
            cur.execute("""INSERT INTO my_place (country, place) VALUES (%s, %s) RETURNING id_place""",
                        ('some place', place))
            id_place = cur.fetchone()[0]
            conn.commit()
        else:
            id_place = id_place[0]

        cur.close()
        conn.close()

        return id_place

    def dump_rasasi_database(self):
        if platform == 'linux':
            cTime = datetime.datetime.now().date() - datetime.timedelta(days=1)
            path = fr'/home/rasasi/dump_database_rasasi/{cTime}.sql'
            process = subprocess.Popen(fr'pg_dump rasasi_database > {path}', shell=True, executable='/bin/bash')
            process.terminate()
            GoogleDrive().upload(files=path, folder_id='1CpsaUbjn2_4Zm6Sog05BBQwf3MEqQ2Vk')
            print('DATABASE DUMP WAS SUCCESS')
        else:
            print(f'Платформа {platform} не поддерживается\nБэкап базы данных не совершён')

    def daily_forecast(self, upass):

        """

        :return: список с ['датавремя - осадки',]
        """
        precipitation_forecast = []
        conn = psycopg2.connect(dbname='rasasi_database', user='rasasi', password=upass, host='localhost')
        cur = conn.cursor()

        cur.execute(
            """SELECT * FROM "weather_journal" WHERE (
            "time" >= %s AND 
            "time" < %s AND 
            "precipitation_mm" > 0 AND 
            "id_place" = 1)""", (
            datetime.datetime.today().date(),
            datetime.datetime.today().date()+datetime.timedelta(days=1)))
        response = cur.fetchall()

        for i in response:
            precipitation_forecast.append(str(i[3]) + ' - ' + str(i[5]) + ' мм 🌧')

        cur.close()
        conn.close()

        if precipitation_forecast:
            return precipitation_forecast
        else:
            precipitation_forecast.append('Без осадков☀☺')
            return precipitation_forecast

    def append_database_today_weather(self, values, upass):

        """

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
        print('weather successfully added to database ☁  😊')

    def lenta_discount(self, upass, discount):
        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""INSERT INTO lenta_discount (date, discount) VALUES (current_date, %s)""", (discount,))

        conn.commit()
        cur.close()
        conn.close()