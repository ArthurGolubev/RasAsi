# from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet
import psycopg2
# k = GoogleSpreadsheet().get_spreadsheets_values(spreadsheet_id='1fgjOxFNxjnUIRRIA60xnWCpYyLRg0txuazimsbg1Km4', range_name='Лист1')
# print(k)

conn = psycopg2.connect(dbname='postgres', user='postgres', password='HOPPOH77', host='localhost')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS "my_city" (id_city serial PRIMARY KEY, country varchar(20), city varchar(20))')
cur.execute('CREATE TABLE IF NOT EXISTS "weather_journal" ('
            'id_weather_journal serial PRIMARY KEY,'
            'id_city )')
# cursor.execute('SELECT * FROM "date_day" WHERE ("date_day" = current_date)')
# cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")
# c = cursor.fetchall()
# print(c)
# cur.execute('INSERT INTO "my_city" VALUES (DEFAULT, %s, %s)', ( "Russia", "Krsk"))
cur.execute('SELECT * FROM "my_city"')
c2 = cur.fetchall()
print(c2)

conn.commit()
cur.close()
conn.close()
