import asyncio
from ble.discover import scan
from cypher.make_key import make_key
#処理を書く

#端末のスキャン
df = asyncio.run(scan())

print(df)

#鍵の作成
secret_key,public_key = make_key()

print(secret_key)
print(public_key)