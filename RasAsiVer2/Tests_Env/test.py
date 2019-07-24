# from RasAsiVer2.Database.RasAsiDatabase import RasAsiDatabase
# from RasAsiVer2.Google.GoogleTasks import GoogleTasks
from RasAsiVer2.Time_Packeg.TodayTasks_v2 import TodayTasksV2
from RasAsiVer2.Database.CreateTables import CreateTables


p = TodayTasksV2(upass=input('pass '))
# CreateTables(upass=input('upass - ')).create_first_tags()
# p.get_3_tasks()
p.refresh_v2()