import platform    
import subprocess 
import sys

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    final = ''

    if subprocess.call(command) == 0:
        final = 'UP'
    else:
        final = 'DOWN'
    return print(final)

args = str(sys.argv[1])
ping(args)