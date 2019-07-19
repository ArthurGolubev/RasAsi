from RasAsiVer2.Google.GoogleTasks import GoogleTasks
from  datetime import datetime, timedelta

cTime = datetime.now().time()

today = (datetime.utcnow() - timedelta(hours=cTime.hour, minutes=cTime.minute, seconds=cTime.second)
                     ).isoformat('T') + 'Z'
t = GoogleTasks(mainID='MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow').list_tasks()
print(len(t))
for i in t:
    if i['status'] == 'needsAction':
        print(i)
print(t[0]['status'])