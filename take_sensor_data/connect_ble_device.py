import asyncio
from bleak import BleakClient

address = "CE:19:19:CD:2B:DB"
MODEL_NBR_UUID = "72E3A28D-B994-4F56-BCB4-2FB23733B955"

async def run(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))