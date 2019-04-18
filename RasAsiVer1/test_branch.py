import datetime
from RasAsiVer2.Google.GoogleTasks import GoogleTasks
tl_id ='MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow'

a = GoogleTasks(mainID=tl_id)
w =(datetime.datetime.utcnow() - datetime.timedelta(hours=20)).isoformat('T')+'Z'  # TODO работает
print(w)
a.list_tasks(completedMax=w)
# print(a.get_task(task_id='MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1NjoyMTM5OTUxNTE3ODcyODUz'))

t = datetime.datetime.utcnow()
print(type(t.isoformat('T')))