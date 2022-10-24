import pandas as pd
from ble.discover import scan
import asyncio

def delete_excess_data(df):

    preliminary_data = pd.read_csv('data_folder/事前取得データ.csv')

    #左結合をすることによって，事前に登録されているもののみ残す．
    df = pd.merge(preliminary_data,df, on = 'near_device', how = 'left')
    print(df)

    return df


df = asyncio.run(scan())
delete_excess_data(df)