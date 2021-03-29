import subprocess

p1 = subprocess.Popen(["dmesg"], stdout= subprocess.PIPE)
p2 = subprocess.Popen(["grep", "disk"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()
print(output)