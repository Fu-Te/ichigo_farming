#案１　同時or　
#送信側　1→234に送る仮定　
from concurrent.futures import ThreadPoolExecutor

# ラズパイそれぞれに送信する関数
def toTwo():
    client_thread = threading.Thread(
    target=l2cap_client_for_list(
        bt_addrs, send_data_list))

def toThree():
    client_thread = threading.Thread(
    target=l2cap_client_for_list(
        bt_addrs, send_data_list))

def toFour():
    client_thread = threading.Thread(
    target=l2cap_client_for_list(
        bt_addrs, send_data_list))

#送信はまとめて
def SEND():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(toTwo())
        executor.submit(toThree())
        executor.submit(toFour())

#受信側　それぞれから受信×3 
# これ同時にやったら良い感じにならない？
# 多分必要なもの：それぞれの流れを合わせる何か？いらない？
# 4基で試してみたい　（意味あるかないかも含めて）

#案2　時間制　
