import platform as p
import subprocess as sub
import sys

try:
    inputos = str(sys.argv[1])
except IndexError:
    inputos = 'null\n\nGagal:IP address belum diberikan\nContoh: check_host.py 192.168.1.1\n\n'

systemos = '-n' if p.system().lower() == 'windows' else '-c'
ping = ['ping', systemos, '3', inputos]

status = ''

if sub.call(ping) == 0:
    status = 'UP'
else:
    if IndexError:
        status = ''
    else:
        status = 'DOWN'

print(status)
