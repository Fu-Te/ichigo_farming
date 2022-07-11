import subprocess
status, output = subprocess.getstatusoutput('hciconfig')
output = output.split('hci0:')[1].split('BD Address: ')[1].split(' ')[0]
print(output)
