from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet
import psycopg2
import getpass
from psycopg2.extras import execute_values



def add_awesome_stuff(city_weather, city_num, upass, today_id):

    # k = GoogleSpreadsheet().get_spreadsheets_values(spreadsheet_id='1fgjOxFNxjnUIRRIA60xnWCpYyLRg0txuazimsbg1Km4',
    #                                                 range_name='Лист1')
    # n = GoogleSpreadsheet().get_spreadsheets_values(spreadsheet_id='1LZF9yopCmDpUUkjSPSu4krwwJ0IFOHV7Qioz_4SuFm0',
    #                                                 range_name='Лист1')
    # print(k['values'][1])
    # user_password = getpass.getpass(prompt='Пароль БД:')

    some_some_dict = []
    for i in city_weather['values'][1:]:
        some_dict = []
        temp_dict = []
        temp_dict.append(city_num)
        temp_dict.append(today_id)
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
    conn = psycopg2.connect(dbname='postgres', user='postgres', password=upass, host='localhost')
    cur = conn.cursor()

    # cur.execute('DROP TABLE IF EXISTS "weather_journal"')

    # cur.execute('CREATE TABLE IF NOT EXISTS "my_city" ('
    #             'id_city serial PRIMARY KEY, '
    #             'country varchar(20), '
    #             'city varchar(20))')

    cur.execute("""CREATE TABLE IF NOT EXISTS my_place (
    id_place serial PRIMARY KEY,
    country varchar(20), 
    city varchar(20))""")

    # cur.execute('CREATE TABLE IF NOT EXISTS "weather_journal" ('
    #             'id_weather_journal serial PRIMARY KEY,'
    #             'id_city integer REFERENCES "my_city",'
    #             'id_date_day integer REFERENCES "date_day",'
    #             'time timestamp,'
    #             'Wind_mps int,'
    #             'Precipitation_mm real,'
    #             'Temperature_c integer,'
    #             'Cloudiness_percent integer,'
    #             'Humidity_percent integer,'
    #             'Atmosphere_pressure_hpa integer,'
    #             'Atmosphere_pressure_mmhg integer)')

    cur.execute("""CREATE TABLE IF NOT EXISTS "weather_journal" (
    id_weather_journal serial PRIMARY KEY, 
    id_city integer REFERENCES my_city,  
    time timestamp, 
    wind_mps integer, 
    precipitation_mm real, 
    temperature_c integer, 
    cloudiness_percent integer, 
    humidity_percent integer, 
    atmosphere_pressure_hpa integer, 
    atmosphere_pressure_mmhg integer)""")



    # execute_values(cur, 'INSERT INTO "weather_journal" ('
    #                     'id_city, id_date_day, time, Wind_mps, Precipitation_mm, Temperature_c, Cloudiness_percent,'
    #                     'Humidity_percent, Atmosphere_pressure_hpa, Atmosphere_pressure_mmhg)'
    #                     ' VALUES %s', some_some_dict)

    execute_values(cur, """INSERT INTO weather_journal (
    id_city, time, wind_mps, precipitation_mm, temperature_c, cloudiness_percent, humidity_percent, 
    atmosphere_pressure_hpa, atmosphere_pressure_mmhg VALUES %s)""", some_some_dict)

    # [(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    # cur.execute('SELECT * FROM "weather_journal"')
    # k = cur.fetchall()
    # print(k)
    # cursor.execute('SELECT * FROM "date_day" WHERE ("date_day" = current_date)')
    # cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")
    # c = cursor.fetchall()
    # print(c)
    # cur.execute('INSERT INTO "my_city" VALUES (DEFAULT, %s, %s)', ( "Russia", "Krasnoyarsk"))
    # cur.execute('INSERT INTO "my_city" VALUES (DEFAULT, %s, %s)', ( "Russia", "Novosibirsk"))
    # cur.execute('SELECT * FROM "my_city"')
    # c2 = cur.fetchall()
    # print(c2)

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    add_awesome_stuff(n, 2, upass=input('pass')) # TODO указать сегодняшний день в TimeManagement
    add_awesome_stuff(k, 1, upass=input('pass')) # TODO указать сегодняшний день в TimeManagement