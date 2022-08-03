from http import server
import bluetooth


def l2cap_server():
    server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
    server_sock.bind(('',0x1001))
    server_sock.listen(1)

    while True:
        print('送信されてくるデータを待ってます')
        client_sock, address = server_sock.accept()
        print(f'データを受け取りました{str(address)}')
        
        print('データを受信中')
        
        total = 0
        total_data = ''
        while True:
            try:
                data = client_sock.recv(1024)
            except bluetooth.BluetoothError as e:
                break
            
            if len(data) == 0:
                break
            
            total += len(data)
            
            print(f'total byte read:{total}')
            print(f'data is: {data}')
            
        client_sock.close()
        
        print('connection closed')
        
    server_sock.close()
    
    return data

data = l2cap_server()