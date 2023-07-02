import os 
import subprocess
import re
os.system('netsh wlan show profiles > output.txt')

with open('output.txt') as file:
    content = file.read()

pattern  =r"(?<=:)\s*(.*?)(?=\n|$)"
matches = re.findall(pattern,content)

for i in matches:
    command = f'netsh wlan show profiles name="{i}" key=clear'
    result = subprocess.run(command,capture_output=True,text=True,shell=True)
    output = result.stdout
    
    pattern2 = r"Key Content\s*: (.*)"
    match = re.search(pattern2,output)
    if match:
        key_content = match.group(1)
        print(f'[*] Password for {i} is {key_content}')