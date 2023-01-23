# addressを探すためのコード
import asyncio
import pandas as pd

from bleak import BleakScanner


async def scan():
    """
    周囲のデバイスをスキャンし，端末名とアドレスをデータフレーム形式で出力する

    Parameters
    ----------


    Return
    ----------
    df : DataFrame
        周囲のBLEでスキャンできるすべての端末情報

    Notes
    ----------
    """
    raw_data = []
    bt_addrs = []
    device_name = []

    devices = await BleakScanner.discover()
    for d in devices:
        raw_data.append(d)

        d, c = str(d).split(': ')
        bt_addrs.append(d)
        device_name.append(c)

    df = pd.DataFrame(list(zip(bt_addrs, device_name)),
                        columns=['bt_addrs', 'device_name'])
    
    return bt_addrs,device_name
