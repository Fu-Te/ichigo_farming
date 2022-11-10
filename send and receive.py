# 案１　同時or　
# 送信側　1→234に送る仮定　
from concurrent.futures import ThreadPoolExecutor
# ラズパイそれぞれに送信する関数

def toTwo(bt_addrs, data):
    client_thread = threading.Thread(
        target=l2cap_client(
        bt_addrs[0], send_data_list[0][0]))
    
def toThree(bt_addrs, data):
    client_thread=threading.Thread(
        target=l2cap_client(
        bt_addrs[1], send_data_list[0][0]))
        

def toFour(bt_addrs, data):
    client_thread=threading.Thread(
        target=l2cap_client(
        bt_addrs[2], send_data_list[0][0]))

# 送信はまとめて
def SEND():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(toTwo())
        executor.submit(toThree())
        executor.submit(toFour())

# 受信側　それぞれから受信×3
# これ同時にやったら良い感じにならない？
# 多分必要なもの：それぞれの流れを合わせる何か？いらない？
# 4基で試してみたい　（意味あるかないかも含めて）
# 案2　時間制
