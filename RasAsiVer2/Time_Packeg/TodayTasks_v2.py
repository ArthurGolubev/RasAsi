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
        self.snapshot_my_storage()

    def snapshot_my_storage(self):
        conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=self._upass, host='localhost')
        cur = conn.cursor()

        cur.execute("""SELECT id_storage, content FROM my_storage WHERE (completed = FALSE)""")
        self._snapshot_my_storage = cur.fetchall()

        cur.close()
        conn.close()

    def get_3_tasks(self, n=None):

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
                GoogleTasks(mainID=self._tasklist_id).insert(task={'title': i[1]})
                break

    def refresh_v2(self):
        """
        Shows completed today (from 00:00 today). Checks for tags. Marks the event in the corresponding tag table
        :return:
        """
        self.snapshot_my_storage()
        cTime = datetime.now().time()
        today = (datetime.utcnow() - timedelta(hours=cTime.hour, minutes=cTime.minute, seconds=cTime.second)
                 ).isoformat('T') + 'Z'
        completed_tasks = GoogleTasks(mainID='MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow'
                                      ).list_tasks(completedMin=today)

        for i in completed_tasks:
            id_task = None

            for i2 in self._snapshot_my_storage:
                if i2[1] == i['title']:
                    id_task = i2[0]
                    break

            conn = psycopg2.connect(database='rasasi_database', user='rasasi', password=self._upass, host='localhost')
            cur = conn.cursor()

            if i.get('notes') and id_task:
                tags = i['notes'].split('#')[1:]
                comment = i['notes'].split('#')[0]

                for tag in tags:
                    print(f'tag - {tag}')
                    if tag.startswith('daily_sp'):
                        print('daily_sp - ok')
                        cur.execute("""INSERT INTO daily_ach (date, daily_sp) VALUES (current_date, True) 
                        ON CONFLICT (date) DO UPDATE SET daily_sp = True""")
                    elif tag.startswith('daily_rs_ins'):
                        print('daily_rs_ins - ok')
                        cur.execute("""INSERT INTO daily_ach (date, daily_rs_ins) VALUES (current_date, True) 
                        ON CONFLICT (date) DO UPDATE SET daily_rs_ins = True""")
                    elif tag.startswith('daily_read'):
                        print('daily_read - ok')
                        cur.execute("""INSERT INTO daily_ach (date, daily_read) VALUES (current_date, True) 
                        ON CONFLICT (date) DO UPDATE SET daily_read = True""")

                    elif tag.startswith('python'):
                        cur.execute("""INSERT INTO first_tags (python, rid_my_storage) VALUES (%s, %s)""", (True, id_task))
                    elif tag.startswith('rs'):
                        cur.execute("""INSERT INTO first_tags (rs, rid_my_storage) VALUES (%s, %s)""", (True, id_task))
                    elif tag.startswith('other'):
                        cur.execute("""INSERT INTO first_tags (other, rid_my_storage) VALUES (%s, %s)""", (True, id_task))


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

        cur.execute("""INSERT INTO my_storage (date_added, content) VALUES (current_date, %s) RETURNING id_storage""",
                    (content,))
        id_task = cur.fetchone()[0]

        tags = content.split('#')
        if len(tags) > 1:
            for tag in tags[1:]:
                if tag.startswith('python'):
                    cur.execute("""INSERT INTO first_tags (python, rid_my_storage) VALUES (%s, %s)""", (True, id_task))
                elif tag.startswith('rs'):
                    cur.execute("""INSERT INTO first_tags (rs, rid_my_storage) VALUES (%s, %s)""", (True, id_task))
                elif tag.startswith('other'):
                    cur.execute("""INSERT INTO first_tags (other, rid_my_storage) VALUES (%s, %s)""", (True, id_task))

        conn.commit()
        cur.close()
        conn.close()

    def clear_v2(self):
        Tasks = GoogleTasks(mainID=self._tasklist_id).list_tasks()
        for i in Tasks:
            due = i.get('due')
            if i['status'] == 'needsAction' and not due:
                GoogleTasks(mainID=self._tasklist_id).delete_task(task_id=i['id'])
        self._DailyTasks.clear()
        self._snapshot_my_storage.clear()
        self.snapshot_my_storage()


if __name__ == '__main__':
    # TodayTasksV2(upass=input('pass ')).get_3_tasks()
    TodayTasksV2(upass=input('pass ')).refresh_v2()