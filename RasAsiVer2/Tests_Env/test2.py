# bashCommand = r"cd C:\Program Files\PostgreSQL\11\bin"
# bashCommand2 = r"C:\Program Files\PostgreSQL\11\bin>pg_dump.exe --role=postgres --username=postgres postgres > C:\Users\ArthurGo\Desktop\1\p2.sql"
import subprocess


def bash_command(c):
    subprocess.Popen(c, shell=True, executable='/bin/bash')


if __name__ == '__main__':
    bash_command(r'pg_dump --role=postgres --username=postgres postgres > backup.sql')

