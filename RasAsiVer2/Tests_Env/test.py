import psycopg2

def test(upass):
    conn = psycopg2.connect(database='postgres', user='postgres', password=upass, host='localhost')
    cur = conn.cursor()
    tag_id = 400
    tag_line = 'sql, python'
    tag_line2 = ['sql', 'python']
    # t_l = tag_line.split(',')
    cur.execute("""INSERT INTO tag_table (rid_storage, {0}, {2}) VALUES (407, {1}, {1})""".format('sql', True, 'python', False))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    test(upass=input('pass '))