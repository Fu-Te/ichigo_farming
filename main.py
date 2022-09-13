import asyncio
import json


from ble.discover import scan
from cipher.cipher import make_key
from cipher.cipher import judge_signature
from cipher.cipher import make_signature

#from ble.l2cap_server import l2cap_server
#from ble.l2cap_client import l2cap_client

#設定用

#ビーコンのアドレス一覧(自分の端末以外のアドレスを指定)
json_file = open('settings.json', 'r')
json_data = json.load(json_file)

bt_addrs =[]

for bt_addr in json_data.values():
    bt_addrs.append(bt_addr)


#送信するデータの格納用リスト
#[df, public_key, signature]
send_data_list = []

#受け取る情報の格納用リスト
#[[df, public_key, signature],[df, public_key, signature]]のような構成になる．
#取り出すためにはreceive_data_list[1][0]みたいな感じで使う
receive_data_list = []

#鍵の作成
secret_key,public_key = make_key()


#処理を書く

#他の端末に送信する情報の作成
#端末のスキャン
df = asyncio.run(scan())

print(df)



#署名の作成
signature = make_signature(secret_key, df)

#送信用データの作成
send_data_list.append(df)
send_data_list.append(public_key)
send_data_list.append(signature)

print(send_data_list)

"""
#データの送信
for bt_addr in bt_addrs:
    l2cap_client(bt_addr, send_data_list)


#データの受信
count = 0
while True:
    data = l2cap_server()
    receive_data_list.append(data)
    count = count + 1
    if count > 4:
        break
"""

#署名の検証
result = judge_signature(signature, df , public_key)
print(result)

