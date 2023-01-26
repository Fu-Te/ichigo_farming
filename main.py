import asyncio
import json
import threading
import time

import pandas as pd

import blockchain.myblock
from ble.discover import scan
from ble.l2cap_client import l2cap_client_for_list
from ble.l2cap_server import l2cap_server
from ble.start_discoverable import start_discoverable
from cipher.cipher import judge_signature, make_key, make_signature
from delete_excess_data import delete_excess_data
from pandas_d_encode import pandas_decode, pandas_encode
from send_and_receive import SEND

# from ble.l2cap_server import l2cap_server
# from ble.l2cap_client import l2cap_client

# 設定用

# ビーコンのアドレス一覧(自分の端末以外のアドレスを指定)
json_file = open("settings1.json", "r")
json_data = json.load(json_file)

tanmatsu_bt_addrs = []

for bt_addr in json_data.values():
    tanmatsu_bt_addrs.append(bt_addr)

print(tanmatsu_bt_addrs)

# 送信するデータの格納用リスト
# [df, public_key, signature]
send_data_list = []

# 受け取る情報の格納用リスト
# [[df, public_key, signature],[df, public_key, signature]]のような構成になる．
# 取り出すためにはreceive_data_list[1][0]みたいな感じで使う
receive_data_list = []

# 鍵の作成
secret_key, public_key = make_key()


# 処理を書く

# 他の端末に送信する情報の作成
# 端末のスキャン
bt_addrs, device_name = asyncio.run(scan())
df = pd.DataFrame(list(zip(bt_addrs, device_name)), columns=["bt_addrs", "device_name"])
df = delete_excess_data(df)

bytes_df = pandas_encode(df)


# 署名の作成
signature = make_signature(secret_key, df)

# 送信用データの作成
send_data_list.append(bytes_df)
send_data_list.append(public_key)
send_data_list.append(signature)


# ↑まで完成
# 以下のプログラムの改善が必要，部品はまあまあできている


# データの受信
# discoverable on
start_discoverable()


# 送受信の実行
SEND(tanmatsu_bt_addrs, send_data_list)
start_discoverable()
receive_data_list.append(l2cap_server())
time.sleep(30)
start_discoverable()
receive_data_list.append(l2cap_server())
time.sleep(30)
start_discoverable()
receive_data_list.append(l2cap_server())

# 署名の検証
count = 0
# それぞれの端末の情報について署名を検証し，結果をリストに格納する．
for i in receive_data_list:
    df = pandas_decode(i[0])
    i[0] = df
    result = judge_signature(i[2], i[0], i[1])
    receive_data_list[count].append(result)
    count = count + 1
    print(result)


# blockchainに追加
blockchain = blockchain.myblock.MyBlockChain()
blockchain.myblock.make_blockchain(receive_data_list)
blockchain.dump()
