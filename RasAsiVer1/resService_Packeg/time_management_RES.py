import threading
from RasAsiVer1.Time_Packeg.time_management import k2


def time_managment_RES(t_stop):
    print(t_stop)
    t_stop.clear()
    t2 = threading.Thread(target=k2, name='T_time_manegement', args=(t_stop,))
    t2.start()
