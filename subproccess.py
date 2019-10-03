import subprocess

try:
    proc = subprocess.run(["python3.6", "/home/arthur5233/mysite/alpha/vk_acc_with_longLINDA.py"], stdout=subprocess.PIPE, timeout=60*60)
    print(proc.stdout.decode('ascii'))
except subprocess.TimeoutExpired:
    print('Process ran too long and was killed.')