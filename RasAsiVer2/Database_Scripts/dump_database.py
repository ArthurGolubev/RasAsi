import subprocess, datetime
from RasAsiVer2.Google.GoogleDrive import GoogleDrive


def dump_rasasi_database():
    cTime = datetime.datetime.now().date()-datetime.timedelta(days=1)
    print(cTime)
    path = f'/home/rasasi/dump_database_rasasi/{cTime}.sql'
    subprocess.Popen(f'pg_dump rasasi_database > {path}')
    GoogleDrive().upload(files=path)

if __name__ == '__main__':
    dump_rasasi_database()