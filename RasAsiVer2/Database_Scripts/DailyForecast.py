import psycopg2
import datetime


class DailyForecast:
    def __init__(self, upass):
        self.upass = upass

    def get_today_precipitation(self):

        """

        :return: список с ['датавремя - осадки',]
        """
        precipitation_forecast = []
        conn = psycopg2.connect(dbname='rasasi_database', user='rasasi', password=self.upass, host='localhost')
        cur = conn.cursor()

        cur.execute(
            """SELECT * FROM "weather_journal" WHERE (
            "time" >= %s AND 
            "time" < %s AND 
            "precipitation_mm" > 0 AND 
            "id_city" = 1)""", (  # TODO поменять город на динамическую переменную
            datetime.datetime.today().date(),
            datetime.datetime.today().date()+datetime.timedelta(days=1)))
            # (datetime.datetime.today()-datetime.timedelta(days=5)).date(),
            # datetime.datetime.today().date()))
        response = cur.fetchall()

        for i in response:
            # print(i[3], '-', i[5], '🌧')
            precipitation_forecast.append(str(i[3]) + ' - ' + str(i[5]) + ' мм 🌧')

        # print(precipitation_forecast)

        cur.close()
        conn.close()

        if precipitation_forecast:
            return precipitation_forecast
        else:
            precipitation_forecast.append('Без осадков☀☺')
            return precipitation_forecast


if __name__ == '__main__':
    DailyForecast(upass=input('pass ')).get_today_precipitation()