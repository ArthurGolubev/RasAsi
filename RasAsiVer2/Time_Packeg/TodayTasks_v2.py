import psycopg2
from random import choice
from datetime import datetime, timedelta
from RasAsiVer2.Google.GoogleTasks import GoogleTasks


class TodayTasksV2:
    _DailyTasks = {}
    _snapshot_my_storage = None
    _tasklist_id = 'MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow'

    def __init__(self, upass):

        self._upass = upass

        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=self._upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""SELECT id_storage, content FROM my_storage WHERE (completed = FALSE)""")
        self._snapshot_my_storage = cur.fetchall()

        print(self._snapshot_my_storage)
        cur.close()
        conn.close()
        input('pause\t')

    def get_3_tasks(self, n=None):   # TODO может сделать один снимок базы my_storage при инициализации объекта класса?

        if not n:
            n = 3
        if len(self._snapshot_my_storage) < 3:
            n = len(self._snapshot_my_storage)
        while n:
            random_choice = choice(self._snapshot_my_storage)
            if not random_choice[1] in self._DailyTasks.keys():
                self._DailyTasks.update({random_choice[1]: random_choice[0]})
                GoogleTasks(mainID=self._tasklist_id).insert(task={'title': random_choice[1]})
                n -= 1

        print('3 Tasks\t', self._DailyTasks)

    def get_specific_one_v2(self, num):
        """

        :param num: id specific entry
        :return: Nothing
        """
        for i in self._snapshot_my_storage:
            if i[0] == num:
                GoogleTasks(mainID=self._tasklist_id).insert(task={i[1]})

    def refresh_v2(self):  # TODO метод ещё не сделан
        """
        Shows completed today (from 00:00 today). Checks for tags. Marks the event in the corresponding tag table
        :return:
        """
        cTime = datetime.now().time()
        today = (datetime.utcnow() - timedelta(hours=cTime.hour, minutes=cTime.minute, seconds=cTime.second)
                 ).isoformat('T') + 'Z'
        completed_tasks = GoogleTasks(mainID='MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow'
                                      ).list_tasks(completedMin=today)

        for i in completed_tasks:
            print('title\t', i['title'])

            conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=self._upass, host='localhost')
            cur = conn.cursor()

            for i2 in self._snapshot_my_storage:
                if i2[1] == i['title']:
                    print('stop - i title - ', i['title'], 'id - ', i2[0])
                    id_task = i2[0]
                    print('id- tasks - ', id_task)
                    input('pauseSTOPE\t')
                    break

            if i.get('notes'):
                tags = i['notes'].split('#')[1:]
                comment = i['notes'].split('#')[0]
                print('comment - \t', comment, '\n tag - ', tags)
                for tag in tags:
                    if tag.startswith('daily_sp'):
                        cur.execute("""INSERT INTO daily_ach (date, daily_sp) VALUES (current_date, True)""")
                    elif tag.startswith('daily_rs_ins'):
                        cur.execute("""INSERT INTO daily_ach (date, daily_rs_ins) VALUES (current_date, True)""")
                    elif tag.startswith('daily_read'):
                        cur.execute("""INSERT INTO daily_ach (date, daily_read) VALUES (current_date, True)""")

                    elif tag.startswith('python'):
                        print('python tag')
                        print('id ', id_task)
                        cur.execute("""INSERT INTO first_tags (python, rid_my_storage) VALUES (%s, %s)""", (True, id_task))

                cur.execute("""UPDATE my_storage SET completed = True, date_completed = current_date, comment = %s 
                                WHERE (id_storage = %s)""", (comment, id_task))             # обновление my_storage
            else:
                cur.execute("""UPDATE my_storage SET completed = True, date_completed = current_date 
                WHERE (id_storage = %s)""", (id_task,))                                     # обновление my_storage

            conn.commit()
            cur.close()
            conn.close()

    def put_v2(self, content):
        """

        :param content: string from msg
        :return: None
        """
        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=self._upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""INSERT INTO my_storage (date_added, content) VALUES (current_date, %s)""", (content,))

        conn.commit()
        cur.close()
        conn.clos()

    def clear_v2(self):
        Tasks = GoogleTasks(mainID=self._tasklist_id).list_tasks()
        for i in Tasks:
            due = i.get('due')
            if i['status'] == 'needsAction' and not due:
                GoogleTasks(mainID=self._tasklist_id).delete_task(task_id=i['id'])
        self._DailyTasks.clear()
        self._snapshot_my_storage.clear()


if __name__ == '__main__':
    # TodayTasksV2(upass=input('pass ')).get_3_tasks()
    TodayTasksV2(upass=input('pass ')).refresh_v2()