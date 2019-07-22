import psycopg2
import datetime
from psycopg2.extras import execute_values
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet


def migration_weather_journal(upass):
    storage_data = GoogleSpreadsheet().get_spreadsheets_values(
        spreadsheet_id='1DvY6qzp32qP_BNTFU2opXlfQ0lpnjs1MnGZ7LWRJIbw',
        range_name='Лист1')['values']

    print(storage_data)
    conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=upass, host='localhost')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS my_storage (
    id_storage serial PRIMARY KEY, 
    date_added date, 
    content text, 
    completed boolean, 
    data_completed date NULL, 
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
                   """INSERT INTO my_storage(date_added, content, completed, data_completed, comment) VALUES %s""",
                   test_list)

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    migration_weather_journal(upass=input('pass '))