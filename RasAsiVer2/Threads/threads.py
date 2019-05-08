import time
import threading
from RasAsiVer2.Google.GoogleGmail import GoogleGmail
from RasAsiVer2.Time_Packeg.TimeManagement import TimeManagement


def start_threads():
    t1.start()
    t2.start()


def checker():
    switch = 0
    while True:
        if not t1.is_alive() and not switch:
            try:
                with open('logfile.txt', 'r') as file:
                    GoogleGmail().send_message(topic=f'😒 Thread is down 🌫',
                                               message_text=file.read())
                switch = 1

            except:
                time.sleep(60)
        time.sleep(60)


t1 = threading.Thread(target=TimeManagement().time_line, name='T_TimeManagement')
t2 = threading.Thread(target=checker, name='check thread TimeManagement')

if __name__ == '__main__':
    start_threads()
else:
    print(f'Подключен модуль {__name__}')