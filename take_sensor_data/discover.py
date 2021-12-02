# addressを探すためのコード
import asyncio

from bleak import discover


def scan():
    async def run():
        devices = await discover()
        for d in devices:
            print(d)

    loop = asyncio.get_event_loop()
    return loop.run_until_complete(run())


scan()