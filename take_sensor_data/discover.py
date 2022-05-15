# addressを探すためのコード
import asyncio
import hashlib

from bleak import BleakScanner

near_device=[]
hash_device=[]

async def scan():
    devices = await BleakScanner.discover()
    for d in devices:
        d,c=str(d).split(':')
        near_device.append(d)
        
        
        d=hashlib.md5(d.encode()).hexdigest()
        hash_device.append(d)
        

asyncio.run(scan())




print(near_device)
print(hash_device)