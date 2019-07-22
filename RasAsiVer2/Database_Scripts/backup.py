import subprocess

def backup():
    command = 'pg_backup'
    subprocess.Popen(command, shell=True, executable='/bin/bash')
