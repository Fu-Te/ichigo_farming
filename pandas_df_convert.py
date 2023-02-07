import io
import pandas as pd

def encode_df(df):
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    return buf.getvalue().encode()

def decode_df(encoded_df):
    buf = io.StringIO(encoded_df.decode())
    return pd.read_csv(buf)
