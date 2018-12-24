import datetime, time

dtime = datetime.timedelta(seconds=int(5231)).total_seconds()
print(dtime)
print('hour=', int(dtime/3600))
print('min=', int((dtime%3600)/60))
print('sec=', (dtime%60))