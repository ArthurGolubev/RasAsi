from RasAsiVer2.Database.RasAsiDatabase import RasAsiDatabase
# from RasAsiVer2.Google.GoogleTasks import GoogleTasks
# from RasAsiVer2.Time_Packeg.TodayTasks_v2 import TodayTasksV2
# from RasAsiVer2.Database.CreateTables import CreateTables


p = RasAsiDatabase().daily_forecast(upass=input('pass '))
print(p)