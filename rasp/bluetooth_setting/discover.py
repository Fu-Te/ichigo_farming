# addressを探すためのコード
import asyncio
import pandas as pd

from bleak import BleakScanner

async def scan():
    raw_data = []
    near_device = []
    device_name = []
    
    
    devices = await BleakScanner.discover()
    for d in devices:
        raw_data.append(d)

        d,c = str(d).split(': ')
        near_device.append(d)
        device_name.append(c)
        
        df = pd.DataFrame(list(zip(near_device, device_name)), columns = ['near_device', 'device_name'])
        print(df)
    return df
asyncio.run(scan())

