import io

import openpyxl
import pandas as pd


def pandas_encode(df):
    """pandas_encode
    データフレームをバイト形式に変換する．

    Parameters
    ----------
    df:DataFrame 変換したいデータフレーム

    Return
    ----------
    バイト形式のDataFrame

    """
    bytes_df = df.to_pickle()

    return bytes_df


def pandas_decode(bytes_df):
    """pandas_decode

    Parameters
    ----------
    df: バイト形式のデータフレーム

    Return
    ----------
    バイト形式でないのデータフレーム

    Args:
        df (_type_): _description_
    """
    df = pd.read_pickle(bytes_df)

    return df
