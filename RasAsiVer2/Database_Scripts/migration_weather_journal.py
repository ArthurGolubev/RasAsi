import psycopg2
from psycopg2.extras import execute_values
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet


def add_awesome_stuff(city_weather, city_num, upass):

    some_some_dict = []
    for i in city_weather['values'][1:]:
        some_dict = []
        temp_dict = []
        temp_dict.append(city_num)
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
    city varchar(30) UNIQUE)""")

    cur.execute("""INSERT INTO my_place (country, city) VALUES ('Russia', 'Krasnoyarsk') ON CONFLICT (city) DO NOTHING""")
    cur.execute("""INSERT INTO my_place (country, city) VALUES ('Russia', 'Novosibirsk') ON CONFLICT (city) DO NOTHING""")

    cur.execute("""CREATE TABLE IF NOT EXISTS "weather_journal" (
    id_weather_journal serial PRIMARY KEY, 
    id_city integer REFERENCES my_place,  
    time timestamp, 
    wind_mps integer, 
    precipitation_mm real, 
    temperature_c integer, 
    cloudiness_percent integer, 
    humidity_percent integer, 
    atmosphere_pressure_hpa integer, 
    atmosphere_pressure_mmhg integer)""")

    execute_values(cur, """INSERT INTO weather_journal (
    id_city, time, wind_mps, precipitation_mm, temperature_c, cloudiness_percent, humidity_percent, 
    atmosphere_pressure_hpa, atmosphere_pressure_mmhg) VALUES %s""", some_some_dict)


    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    k = GoogleSpreadsheet().get_spreadsheets_values(spreadsheet_id='1fgjOxFNxjnUIRRIA60xnWCpYyLRg0txuazimsbg1Km4',
                                                    range_name='Лист1')
    n = GoogleSpreadsheet().get_spreadsheets_values(spreadsheet_id='1LZF9yopCmDpUUkjSPSu4krwwJ0IFOHV7Qioz_4SuFm0',
                                                    range_name='Лист1')
    print(k['values'][1])
    add_awesome_stuff(n, 2, upass=input('pass '))
    add_awesome_stuff(k, 1, upass=input('pass '))