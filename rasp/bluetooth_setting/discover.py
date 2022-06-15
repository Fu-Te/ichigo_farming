# addressを探すためのコード
import asyncio
import hashlib
import pandas as pd

from bleak import BleakScanner

raw_data = []
near_device = []
hash_device = []

async def scan():
    devices = await BleakScanner.discover()
    for d in devices:
        raw_data.append(d)

        d,c = str(d).split(': ')
        near_device.append(d)
        
        
        d = hashlib.md5(d.encode()).hexdigest()
        hash_device.append(d)
        

asyncio.run(scan())

df = pd.DataFrame(list(zip(near_device, hash_device)), columns = ['near_device','hash_device'])

df['device1_flag'] = ''
df['device2_flag'] = ''
df['device3_flag'] = ''
df['device4_flag'] = ''



print(df)
df.to_csv('result/test.csv',index=False , encoding = 'utf_8_sig')