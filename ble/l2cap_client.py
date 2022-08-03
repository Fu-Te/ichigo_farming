import sys
import bluetooth

def l2cap_client(bt_addr,data):
    if sys.version < '3':
        input = raw_input
        
    sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

    if len(sys.argv) < 2:
        print('usage: l2capclient.py <addr>')
        sys.exit(2)
        
    port = 0x1001

    print(f'trying to connect to {bt_addr} on PSM 0x{port}')

    sock.connect((bt_addr,port))

    print('connected. type stuff')

    while True:
        if(len(data) == 0):
            break
        sock.send(data) 
        data = sock.recv(1024)
        print(f'Data received:{str(data)}')
        
    sock.close()
    


bt_addr_list = ['B8:27:EB:7D:E6:F6','E4:5F:01:38:C5:37']
bt_addr = 'E4:5F:01:38:C5:37'
data = 'aaa'


l2cap_client(bt_addr,data)