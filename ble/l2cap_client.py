import sys
import bluetooth


def l2cap_client(bt_addr, data):
    """
    送信したいデータと送信したい相手を指定することでBLE経由でデータを送信することができる.
    l2cap_server.pyを実行している相手に対して情報を送信することができる.

    Parameters
    ----------
    bt_addr : integer
        端末のブルートゥースアドレスを指定する

    data : data
        送信したいデータを指定する

    Return
    ----------


    Notes
    ----------
    タイムアウトを設定したい．一定時間立っても接続できなかった場合はエラーを出るように修正必須

    """
    if sys.version < '3':
        input = raw_input

    sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)


    port = 0x1001

    print(f'trying to connect to {bt_addr} on PSM 0x{port}')

    sock.connect((bt_addr, port))


    sock.send(data)
    data = sock.recv(1024)
    print(f'Data received:{str(data)}')

    sock.close()


def l2cap_client_for_list(bt_addrs, send_data_list):
    """
    bt_addrsを受け取り繰り返しで使う．

    Parameters
    ----------
    bt_addrs : bluetoothアドレスが格納されたリスト
    send_data_list : 送りたい情報
    """
    # データの送信
    for bt_addr in bt_addrs:
        l2cap_client(bt_addr, send_data_list)

l2cap_client('E4:5F:01:38:C5:37','aiueo')