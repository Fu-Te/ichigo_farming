import io


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
    towrite = io.BytesIO()
    df.to_excel(towrite)
    towrite.seek(0)
    bytes_df = towrite.getvalue()
    
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