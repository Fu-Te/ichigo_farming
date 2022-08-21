import asyncio


from ble.discover import scan
from cipher.cipher import make_key
from cipher.cipher import judge_signature
from ble.l2cap_server import l2cap_server
from ble.l2cap_client import l2cap_client

#処理を書く

#ビーコンのアドレス一覧(自分の端末以外のアドレスを指定)
bt_addrs =['B8:27:EB:7D:E6:F6','E4:5F:01:38:C5:37']

#端末のスキャン
df = asyncio.run(scan())

print(df)

#鍵の作成
secret_key,public_key = make_key()

#署名の追加
signature = secret_key.sign(df)

#署名の検証
result = judge_signature(signature, df , public_key)



print(secret_key)
print(public_key)

#情報の暗号化
encrypted_data = df

#公開鍵の送信
for bt_addr in bt_addrs:
    l2cap_client(bt_addr, public_key)


#暗号化されたデータの送信
for bt_addr in bt_addrs:
    l2cap_client(bt_addr, encrypted_data)
    

