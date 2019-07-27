import psycopg2
import datetime
from psycopg2.extras import execute_values
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet


class CreateTables:

    def __init__(self, upass):
        self.upass = upass

    def connection(self, query, arg):
        """

        :param query:
        :param arg: tuple placeholders
        :return:
        """
        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=self.upass)
        cur = conn.cursor()

        respond = cur.execute(query, arg)
        conn.commit()

        cur.close()
        conn.close()
        return respond

    def _migration_weather_journal(self, place_weather, place_num, upass):

        some_some_dict = []
        for i in place_weather['values'][1:]:
            some_dict = []
            temp_dict = []
            temp_dict.append(place_num)
            temp_dict.append(i[0])
            for i2 in i[1:6]:
                t = i2.split(' ')[0].replace(',', '.')

                if not i2:
                    t = None
                temp_dict.append(t)
            temp_dict.append(i[6].split(' ')[0])
            temp_dict.append(i[6].split(' ')[3])
            some_dict.extend(temp_dict)
            some_some_dict.append(tuple(some_dict))

        print(some_some_dict)
        conn = psycopg2.connect(dbname='rasasi_database', user='rasasi', password=upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS my_place (
        id_place serial PRIMARY KEY,
        country varchar(20), 
        place varchar(30) UNIQUE)""")

        cur.execute(
            """INSERT INTO my_place (country, place) VALUES ('Russia', 'Krasnoyarsk') ON CONFLICT (place) DO NOTHING""")
        cur.execute(
            """INSERT INTO my_place (country, place) VALUES ('Russia', 'Novosibirsk') ON CONFLICT (place) DO NOTHING""")

        cur.execute("""CREATE TABLE IF NOT EXISTS "weather_journal" (
        id_weather_journal serial PRIMARY KEY, 
        id_place integer REFERENCES my_place,  
        time timestamp, 
        wind_mps integer, 
        precipitation_mm real, 
        temperature_c integer, 
        cloudiness_percent integer, 
        humidity_percent integer, 
        atmosphere_pressure_hpa integer, 
        atmosphere_pressure_mmhg integer)""")

        execute_values(cur, """INSERT INTO weather_journal (
        id_place, time, wind_mps, precipitation_mm, temperature_c, cloudiness_percent, humidity_percent, 
        atmosphere_pressure_hpa, atmosphere_pressure_mmhg) VALUES %s""", some_some_dict)

        conn.commit()
        cur.close()
        conn.close()

    def ct_m_weather_journal(self):

        k = GoogleSpreadsheet().get_spreadsheets_values(spreadsheet_id='1fgjOxFNxjnUIRRIA60xnWCpYyLRg0txuazimsbg1Km4',
                                                        range_name='Лист1')
        n = GoogleSpreadsheet().get_spreadsheets_values(spreadsheet_id='1LZF9yopCmDpUUkjSPSu4krwwJ0IFOHV7Qioz_4SuFm0',
                                                        range_name='Лист1')

        self._migration_weather_journal(n, 2, upass=self.upass)
        self._migration_weather_journal(k, 1, upass=self.upass)

    def migration_my_storage(self):
        storage_data = GoogleSpreadsheet().get_spreadsheets_values(
            spreadsheet_id='1DvY6qzp32qP_BNTFU2opXlfQ0lpnjs1MnGZ7LWRJIbw',
            range_name='Лист1')['values']

        print(storage_data)
        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=self.upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS my_storage (
        id_storage serial PRIMARY KEY, 
        date_added date, 
        content text, 
        completed boolean, 
        date_completed date NULL, 
        comment text NULL)""")

        test_list = []
        for i in storage_data:
            if len(i) == 3:
                i[0] = datetime.datetime.strptime(i[0], "%d.%m.%Y")
                i.append(None)
                i.append(None)
            elif len(i) > 3:
                i[0] = datetime.datetime.strptime(i[0], "%d.%m.%Y")
                i[3] = datetime.datetime.strptime(i[3], "%d.%m.%Y")
                if len(i) == 4:
                    i.append(None)
            test_list.append(tuple(i))

        execute_values(cur,
                       """INSERT INTO my_storage(date_added, content, completed, date_completed, comment) VALUES %s""",
                       test_list)

        conn.commit()
        cur.close()
        conn.close()

    def create_daily_ach(self):
        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=self.upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS daily_ach (
        id_daily_ach serial PRIMARY KEY, 
        date date UNIQUE, 
        daily_sp boolean NULL, 
        daily_rs_ins boolean NULL, 
        daily_read boolean NULL)""")

        conn.commit()
        cur.close()
        conn.close()

    def create_first_tags(self):
        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=self.upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS first_tags (
        id_tag serial PRIMARY KEY, 
        rid_my_storage int REFERENCES my_storage, 
        python boolean, 
        rs boolean,
        other boolean)""")

        conn.commit()
        cur.close()
        conn.close()

    def create_lenta(self):
        l = GoogleSpreadsheet().get_spreadsheets_values(spreadsheet_id='1SEOxlcQcaVQAhvzAalPUlgpiRWrG0-ji3M8RrZbMnTE',
                                                        range_name='Лист1')['values']

        conn =psycopg2.connect(database='rasasi_database', user='rasasi', password=self.upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS lenta_discount (
        id_discount serial PRIMARY KEY, 
        date date, 
        discount INTEGER)""")

        execute_values(cur, """INSERT INTO lenta_discount (date, discount) VALUES %s""", l)
        conn.commit()
        cur.close()
        conn.close()

    def create_all_tables(self):
        self.create_lenta()
        self.migration_my_storage()
        self.create_first_tags()
        self.create_daily_ach()
        self.ct_m_weather_journal()

if __name__ == '__main__':
    query = """SELECT"""
    somenum = CreateTables(upass=input('pass ')).connection(somfunc=query)
    print(somenum)
