import psycopg2
from random import choice
from datetime import datetime, timedelta
from RasAsiVer2.Google.GoogleTasks import GoogleTasks


class TodayTasksV2:
    DailyTasks = {'4': 2}
    _tasklist_id = 'MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow'

    def __init__(self, upass):
        self.upass = upass

    def get_3_tasks(self, n=None):
        conn = psycopg2.connect(database='postgres', user='postgres', password=self.upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""SELECT id_storage, content FROM my_storage WHERE (completed = FALSE)""")
        tasks = cur.fetchall()

        cur.close()
        conn.close()
        if not n:
            n = 3
        if len(tasks) < 3:
            n = len(tasks)
        while n:
            random_choice = choice(tasks)
            if not random_choice[1] in self.DailyTasks.keys():
                self.DailyTasks.update({random_choice[1]: random_choice[0]})
                GoogleTasks(mainID=self._tasklist_id).insert(task={'title': random_choice[1]})
                n -= 1

        print(self.DailyTasks)

    def refresh_v2(self):
        """
        Shows completed today (from 00:00 today). Checks for tags. Marks the event in the corresponding tag table
        :return:
        """
        if self.DailyTasks:
            print(1)
            cTime = datetime.now().time()
            today = (datetime.utcnow() - timedelta(hours=cTime.hour, minutes=cTime.minute, seconds=cTime.second)
                     ).isoformat('T') + 'Z'
            completed_tasks = GoogleTasks(mainID='MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow'
                                          ).list_tasks(completedMin=today)

            print(completed_tasks[0]['title'])
            print(completed_tasks[0])
        else:
            return

        for i in completed_tasks:
            print(i['title'])

            conn = psycopg2.connect(database='postgres', user='postgres', password=self.upass, host='localhost')
            cur = conn.connect()

            if i['status'] == 'completed':
                id_task = self.DailyTasks.get(i['title'])
                tags = i['notes'].split('#')[1:]

                if i['notes'] == '#daily_sp':
                    cur.execute("""INSERT INTO daily_ach (date, sp) VALUES (current_date, True)""")
                elif i['notes'] == 'daily_rs_ins':
                    cur.execute("""INSERT INTO daily_ach (date, rs_ins) VALUES (current_date, True)""")
                elif i['notes'] == '#daily_read':
                    cur.execute("""INSERT INTO daily_ach (date, read) VALUES (current_date, True)""")

                if tags:  # TODO переделать (два тега на конце не будут считаться)
                    for i in tags:
                       cur.execute("""INSERT INTO tag_table (rid_storage, %s) VALUES ({0}, True) 
                       ON CONFLICT (rid_storage) DO UPDATE SET {1}=True""".format(id_task, i))
                  # TODO проверить тут (Спорт)

                cur.execute("""UPDATE my_storage SET completed = True, date_completed = current_date, comment = %s 
                WHERE (id_storage = %s)""", (i['notes'], id_task))

            conn.commit()
            cur.close()
            conn.close()

    def put_v2(self, content):
        """

        :param content: string from msg
        :return: None
        """
        conn = psycopg2.connect(database='postgres', user='postgres', password=self.upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""INSERT INTO my_storage (date_added, content) VALUES (current_date, %s)""", (content,))

        conn.commit()
        cur.close()
        conn.clos()


if __name__ == '__main__':
    # TodayTasksV2(upass='HOPPOH77').get_3_tasks()
    TodayTasksV2(upass='HOPPOH77').refresh_v2()