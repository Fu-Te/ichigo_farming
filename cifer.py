from ecdsa import SigningKey
from ecdsa import VerifyingKey
from ecdsa import SECP256k1

#ステップ１、秘密鍵・公開鍵の作成

#秘密鍵の作成
secret_key = SigningKey.generate(curve=SECP256k1)
print(secret_key)
#秘密鍵をファイル化
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

#公開鍵の作成
public_key = secret_key.verifying_key
print(public_key)
#公開鍵をファイル化
file_out = open("public.pem", "wb")
file_out.write(public_key)
file_out.close()




#ステップ２　秘密鍵を保管、公開鍵を送信する


#ステップ３　生データに署名を行う

#生データをバイト形式に変換
deta = "送信したい内容の元データ"
deta_bytes = bytes(deta, encoding = "utf-8")
print(deta_bytes)

#生データと秘密鍵から署名データを作成
signature = secret_key.sign(deta_bytes)
print(signature)



#ステップ４　生データと署名データの送付


#ステップ５　受信者がファイルをあける

#公開鍵を用いて署名データと生データで整合性がとれているか確認
public_key.verify(signature, deta_bytes)

#もし整合性がとれていないと（今回は意図的に）
changed_deta = "私はアンパンマンです"
changed_deta_bytes = bytes(changed_deta, encoding = "utf-8")
public_key.verify(signature, changed_deta_bytes)
