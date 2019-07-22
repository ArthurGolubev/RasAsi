import subprocess, datetime
from RasAsiVer2.Google.GoogleDrive import GoogleDrive


def dump_rasasi_database():
    cTime = datetime.datetime.now().date()-datetime.timedelta(days=1)
    path = fr'/home/rasasi/dump_database_rasasi/{cTime}.sql'
    subprocess.Popen(fr'pg_dump rasasi_database > {path}', shell=True, executable='/bin/bash')
    GoogleDrive().upload(files=path, folder_id='1CpsaUbjn2_4Zm6Sog05BBQwf3MEqQ2Vk')
    print('DATABASE DUMP WAS SUCCESS')

if __name__ == '__main__':
    dump_rasasi_database()