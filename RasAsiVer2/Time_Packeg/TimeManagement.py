import threading
from time import sleep
from datetime import datetime
from RasAsiVer1.Gmail_Packeg.Send import send
from RasAsiVer2.Time_Packeg.TodayTasks import TodayTasks
from RasAsiVer1.Time_Packeg.startTimeRasAsi import timeHasPassed, startTimeRasAsi


class TimeManagement:
    Task = TodayTasks()

    def __init__(self, t_stop):
        self.stop = t_stop
        self.T_view_messages = threading.Thread(target=self._view_messages, name='T_viev_messages')
        self.T_server_time = threading.Thread(target=self._server_time, name='T_server_time')
        self.T_Task_put = threading.Thread(target=self._Task_put, name='T_Task_put')
        self.T_Task_give_me_one = threading.Thread(target=self._Task_give_me_one, name='T_Task_give_me_one')
        self.T_Task_check_clean = threading.Thread(target=self._Task_check_clean, name='T_Task_check')

    def time_line(self):
        while not self.stop.is_set():
            cTime = datetime.time()
            self.messages = self._view_messages()
            if 'Время' in self.messages:
                self.T_server_time.start()
            if 'Хранилище' in self.messages:
                self.T_Task_put.start()
            if 'Дай мне один' in self.messages:
                self.T_Task_give_me_one.start()

            if cTime.hour == 0 and cTime.minute == 0:
                self.T_server_time.start()
                self.T_Task_check_clean.start()
            # elif cTime.hour == 2 and:

            elif cTime.hour == 8 and cTime.minute == 0:
                self.Task.take_tasks()

            sleep(60)

    def _view_messages(self):
        input('pause\t')
        return  {} # TODO возращать словарь, где ключ - тема сообщения
        # просмотр сообщений

    def _server_time(self):
        msg = f'🎉👌 Время работы сервера:\t {str(timeHasPassed(startTimeRasAsi))}'
        send(topic='Server time ☁', message=msg)

    def _Task_put(self):
        self.Task.put(material=self.messages.get('Хранилище'))

    def _Task_give_me_one(self):
        self.Task.give_me_one()

    def _Task_check_clean(self):
        self.Task.check()
        self.Task.clean()
