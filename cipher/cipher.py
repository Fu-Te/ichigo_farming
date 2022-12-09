from ecdsa import SigningKey
from ecdsa import VerifyingKey
from ecdsa import SECP256k1
import io
import openpyxl

def make_key():
    """
    通信を暗号化するための秘密鍵と公開鍵を作成する.


    Parameters
    ----------

    Return
    ----------
    secret_s : 秘密鍵
    public_s : 公開鍵

    Notes
    ----------

    """
    secret_key = SigningKey.generate(curve=SECP256k1)
    public_key = secret_key.verifying_key

    return secret_key, public_key


def make_signature(secret_key, df):
    """
    署名を作成するための関数

    Parameters
    ----------
    secret_key : 秘密鍵
    df : 署名を追加したいデータ

    Return
    ----------
    signature : 署名

    Notes
    ----------

    """
    
    #dfをbytes形式に変換
    towrite = io.BytesIO()
    df.to_excel(towrite)
    towrite.seek(0)
    df = towrite.getvalue()
    
    
    signature = secret_key.sign(df)
    return signature


def judge_signature(signature, df, public_key):
    """
    署名の検証
    署名が正しければTrue
    正しくなければFlaseを返す関数



    Parameters
    ----------
    signature : 署名,secret_key.sign(df)で作成したもの.
    df : DetaFrame secret_key.sign(df)で利用したdf
    public_key : 公開鍵

    Return
    ----------
    True : 署名が正しければTrue
    False : 署名が正しくなければFalse

    Notes
    ---------

    """
    
    #dfをbytes形式に変換
    towrite = io.BytesIO()
    df.to_excel(towrite)
    towrite.seek(0)
    df = towrite.getvalue()
    
    #TorF
    result = public_key.verify(signature, df)
    if result == True:
        print('署名が正しいです')
        return result
    else:
        print('署名が正しくありません．')
        return result
