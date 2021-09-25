import asyncio
from bleak import BleakClient

address = "fc:66:cf:be:10:bf"
MODEL_NBR_UUID = "2DE643AA-22A6-460A-A37D-E248D1273502"

async def run(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))