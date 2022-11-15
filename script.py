import subprocess
from time import sleep
from datetime import datetime
def time_now():
    '''Get Current Time'''
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")[:-4]
    print("Current Time =", current_time)
    return now


############
print('Starting...')
start = time_now()
############

sleep(2)
end = time_now()

with open('time.txt',encoding='utf-8', mode='+a') as f:
    if f.tell() != 0:
        f.seek(0)
    f.write(f'Start: {start}, End: {end}\n')

cmd = f"""
git add .
git commit -m "Git pushed from inside python script {end}"
git push origin master  
""".strip().split('\n')

#cmd = [command.split() for command in cmd]

for command in cmd:
    print(command)
    subprocess.run(command)
    print('-------------------------')