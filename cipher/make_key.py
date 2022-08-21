from ecdsa import SigningKey
from ecdsa import VerifyingKey
from ecdsa import SECP256k1

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
    secret_b = secret_key.to_string()
    public_b = public_key.to_string()
    secret_s = secret_b.hex()
    public_s = public_b.hex()
    
    return secret_s, public_s

def signature(signature,df):
    