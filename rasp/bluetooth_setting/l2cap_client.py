import sys
import bluetooth

if sys.version < '3':
    input = raw_input
    
sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

if len(sys.argv) < 2:
    print('usage: l2capclient.py <addr>')
    sys.exit(2)
    
bt_addr = sys.argv[1]
port = 0x1001

print(f'trying to connect to {bt_addr} on PSM 0x{port}')

sock.connect((bt_addr,port))

print('connected. type stuff')

while True:
    data = input()
    if(len(data) == 0):
        break
    sock.send(data) 
    data = sock.recv(1024)
    print(f'Data received:{str(data)}')
    
sock.close()