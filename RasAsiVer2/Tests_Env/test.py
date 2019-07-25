from RasAsiVer2.Database.RasAsiDatabase import RasAsiDatabase
# from RasAsiVer2.Google.GoogleTasks import GoogleTasks
from RasAsiVer2.Time_Packeg.TodayTasks_v2 import TodayTasksV2
from RasAsiVer2.Database.CreateTables import CreateTables


p = TodayTasksV2(upass=input('pass '))
# CreateTables(upass=input('upass - ')).create_lenta()
# RasAsiDatabase().lenta_discount(discount=1000, upass=input('pass '))
p.clear_v2()
# p.get_3_tasks()
# p.refresh_v2()