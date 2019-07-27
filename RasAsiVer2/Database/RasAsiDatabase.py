import psycopg2
import datetime
import subprocess
from sys import platform
from psycopg2.extras import execute_values
from RasAsiVer2.Google.GoogleDrive import GoogleDrive
from RasAsiVer2.Google.GoogleGmail import GoogleGmail


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

    def dump_rasasi_database(self, upass):
        if platform == 'linux':
            cTime = datetime.datetime.now().date() - datetime.timedelta(days=1)
            path = fr'/home/rasasi/dump_database_rasasi/{cTime}'
            with subprocess.Popen(fr'pg_dump rasasi_database > {path}.sql', shell=True):
                print('DATABASE DUMP WAS SUCCESS')
            with subprocess.Popen(fr'7z a -mx0 -sdel -mhe=on -p{upass} {path}.7z {path}.sql', shell=True):
                print('ARCHIVED WITH PASSWORD')
            path = fr'{path}.7z'

            GoogleDrive().upload(files=path, folder_id='1CpsaUbjn2_4Zm6Sog05BBQwf3MEqQ2Vk')
            print('UPLOAD DUMP TO THE CLOUD 👌')
        else:
            print(f'Платформа {platform} не поддерживается\nБэкап базы данных не совершён')

    def daily_forecast(self, upass):

        """

        :return: список с ['датавремя - осадки',]
        """
        forecast = []
        precipitation_forecast= []
        temperature_forecast = []
        wind_forecast = []

        conn = psycopg2.connect(dbname='rasasi_database', user='rasasi', password=upass, host='localhost')
        cur = conn.cursor()

        cur.execute(
            """SELECT * FROM "weather_journal" WHERE (
            "time" >= %s AND
            "time" < %s AND
            "id_place" = 1)""", (
            datetime.datetime.today().date(),
            datetime.datetime.today().date()+datetime.timedelta(days=1)))

        # cur.execute(
        #     """SELECT * FROM weather_journal WHERE (
        #     time >= '2019-07-01' AND
        #     time < '2019-07-02' AND
        #     id_place = 1)"""
        # )
        response = cur.fetchall()

        cur.close()
        conn.close()

        for i in response:
            if i[4] > 0:
                precipitation_forecast.append(str(i[2]).split(' ')[1] + ' - ' + str(i[4]) + ' мм 🌧')
            if i[3] >= 4:
                wind_forecast.append(str(i[2]).split(' ')[1] + ' - ' + str(i[3]) + ' м/с 🌫')
            temperature_forecast.append(str(i[2]).split(' ')[1] + ' - ' + str(i[5]) + ' C ☀')

        if not precipitation_forecast:
            precipitation_forecast.append('Без осадков☀☺')
        if not wind_forecast:
            wind_forecast.append('Безветренно 🌫☺')

        precipitation_forecast = '\n'.join(precipitation_forecast)
        temperature_forecast = '\n'.join(temperature_forecast)
        wind_forecast = '\n'.join(wind_forecast)

        print('\nОсадки:\n', precipitation_forecast)
        print('\nТемпература:\n', temperature_forecast)
        print('\nСкорость ветра:\n', wind_forecast)

        # weather_forecast = f'Погода на {datetime.datetime.today().date()}\n\n' \
        #     f'Осадки:\n{precipitation_forecast}\n\n' \
        #     f'Температура:\n{temperature_forecast}\n\n' \
        #     f'Скорость ветра:\n{wind_forecast}'
        # return weather_forecast

        GoogleGmail().send_message(topic=f'Погода на {datetime.datetime.today().date()}',
                                   message_text=f'Осадки:\n{precipitation_forecast}\n\n'
                                   f'Скорость ветра:\n{wind_forecast}\n\n'
                                   f'Температура:\n{temperature_forecast}'
                                   )


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

    def task_completed_today(self, upass):
        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""INSERT INTO daily_ach (date) VALUES (current_date) ON CONFLICT (date) DO NOTHING""")
        cur.execute("""SELECT COUNT(id_storage) FROM my_storage WHERE(
        date_completed >= current_date)""")
        count1 = cur.fetchone()
        print(count1)
        cur.execute("""SELECT * FROM daily_ach WHERE (date = current_date)""")
        count2 = cur.fetchone()
        print(count2)
        input('pause\t')
        count = count1 + count2
        GoogleGmail().send_message(topic=f'Выполненных за сегодня {datetime.datetime.today().date()}',
                                   message_text=f"Выполнено daily'ков {count2}\n"
                                   f"Выполнено задач {count1}\n"
                                   f"Выполнено в общем {count} 👌☺")

        cur.close()
        conn.close()