# addressを探すためのコード
import asyncio
import hashlib

from bleak import BleakScanner

raw_data=[]
near_device=[]
hash_device=[]

async def scan():
    devices = await BleakScanner.discover()
    for d in devices:
        raw_data.append(d)
        d,c=str(d).split(':')
        near_device.append(d)
        
        
        d=hashlib.md5(d.encode()).hexdigest()
        hash_device.append(d)
        

asyncio.run(scan())



print(raw_data)
print('___________________________________________')
print(near_device)
print('___________________________________________')
print(hash_device)