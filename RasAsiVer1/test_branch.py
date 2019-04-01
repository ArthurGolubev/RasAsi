from RasAsiVer2.Google.GoogleTasks import GoogleTasks
from RasAsiVer2.Time_Packeg.TodayTasks import TodayTasks
f = 'MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njo5MDA1NzY1NzQ1NjAyMjUy'
notes = 'MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njo2MTU0ODI5Njk4MzYzMTYz'
just = 'MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njo3MzQ5NTM2NzIwODk3MDMy'
New_Task = 'MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njo2MTU0ODI5Njk4MzYzMTYz'

lenta ='1SEOxlcQcaVQAhvzAalPUlgpiRWrG0-ji3M8RrZbMnTE'

g = TodayTasks()
# k = GoogleTasks(mainID='MDE2MzQwNDIxMTc3NjI1NjYwMTY6NjU5MTE0NDY0NzQyODU1Njow')
# print(k.get_task(New_Task))
g.take_tasks()
input('pause\t')
g.check()
g.clean()

