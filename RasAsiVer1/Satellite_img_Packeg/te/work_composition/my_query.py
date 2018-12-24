from . import *
zapros1 = 'INSERT INTO calendar(EventDate) VALUE (%s)'
# zapros2 = 'SELECT MAX(EventDate) FROM calendar'
zapros3 = "SELECT EventDate FROM calendar WHERE idCalendar = %s or %s"
zapros4 = "SELECT EventDate FROM calendar WHERE idCalendar = %s"
zapros5 = 'SELECT idCalendar FROM calendar WHERE EventDate = %s'
zapros6 = 'SELECT * FROM metadata WHERE `Title or Event`="over900"'
zapros7 = 'SELECT * FROM metadata WHERE `Title or Event`= %s'
zapros8 = 'INSERT INTO calendar (EventDate) value (20150723115443)'
# zapros9 = 'SELECT idmetadata FROM metadata WHERE `Title or Event` = %s'
# zapros10 = 'INSERT INTO metadata (`Title or Event`, Sourse) VALUE (%s, %s)'
# zapros11 = 'INSERT INTO ' \
#            'satelliteImage (Calendar_idCalendar, metadata_idmetadata, Link, Season, `ovr/tif`, `Image Date`)' \
#            ' VALUES (%s, %s, %s, %s, %s, %s)'

zapros14 = 'SELECT Link FROM satelliteImage JOIN metadate ON metadata_idmetadata = idmetadata WHERE idmetadata = %s'
argument = datetime.datetime.today().date()
argument0 = 'satelliteImage'
argument00 = '1'
argument000 = '3'
argument0000 = datetime.datetime.today()
'''DataBase query'''
DBq1 = 'SELECT idmetadata, `Title or Event` From metadata'
DBq2 = 'SELECT Link FROM satelliteImage JOIN metadata ON metadata_idmetadata = idmetadata WHERE idmetadata = (%s)'
DBq3 = 'UPDATE metadata SET `Download Time` = %s, `Scene Size GB` = %s WHERE `Title or Event` = %s'
DBq4 = 'INSERT INTO ' \
           'satelliteImage (Calendar_idCalendar, metadata_idmetadata, Link, Season, `ovr/tif`, `Image Date`)' \
           ' VALUES (%s, %s, %s, %s, %s, %s)'
DBq5 = 'SELECT idmetadata FROM metadata WHERE `Title or Event` = %s'
DBq6 = 'INSERT INTO metadata (`Title or Event`, Sourse) VALUE (%s, %s)'