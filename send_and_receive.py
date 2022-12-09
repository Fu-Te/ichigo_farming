#案１　同時or　
#送信側　1→234に送る仮定　
from concurrent.futures import ThreadPoolExecutor
import threading
from ble.l2cap_client import l2cap_client
import json

# ラズパイそれぞれに送信する関数
def toTwo(bt_addrs, send_data_list):
    client_thread = threading.Thread(
    target=l2cap_client(
        bt_addrs[0], send_data_list))

def toThree(bt_addrs, send_data_list):
    client_thread = threading.Thread(
    target=l2cap_client(
        bt_addrs[1], send_data_list))

def toFour(bt_addrs, send_data_list):
    client_thread = threading.Thread(
    target=l2cap_client(
        bt_addrs[2], send_data_list))

#送信はまとめて
def SEND(bt_addrs,send_data_list):
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(toTwo(bt_addrs,send_data_list))
        executor.submit(toThree(bt_addrs,send_data_list))
        executor.submit(toFour(bt_addrs,send_data_list))

#受信側　それぞれから受信×3
# これ同時にやったら良い感じにならない？
# 多分必要なもの：それぞれの流れを合わせる何か？いらない？
# 4基で試してみたい　（意味あるかないかも含めて）

#案2　時間制　


if __name__ == '__main__':
    # ビーコンのアドレス一覧(自分の端末以外のアドレスを指定)
    json_file = open('settings.json', 'r')
    json_data = json.load(json_file)

    bt_addrs = []

    send_data = 'ewqkormwqim'

    for bt_addr in json_data.values():
        bt_addrs.append(bt_addr)

    SEND(bt_addrs,send_data)
