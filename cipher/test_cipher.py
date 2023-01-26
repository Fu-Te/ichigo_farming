import pandas as pd
import pytest

from cipher import judge_signature, make_key, make_signature


def test_make_key():
    secret_k, public_k = make_key()
    print(f"秘密鍵{secret_k}:公開鍵{public_k}")

    assert secret_k != ""
    assert public_k != ""


def test_make_signature():
    signature = ""
    secret_k, public_k = make_key()
    df = pd.read_csv("../test_data_folder/cipher/sample1.csv")

    # 署名はbytesにしか対応してない
    signature = make_signature(secret_k, df)
    print(f"署名{signature}")
    assert signature != ""


def test_judge_signature():
    secret_k, public_k = make_key()
    df = pd.read_csv("../test_data_folder/cipher/sample1.csv")
    signature = make_signature(secret_k, df)

    result = judge_signature(signature, df, public_k)

    assert result == True
