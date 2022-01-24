
import logging
 
from bluezero import adapter, device
from bluezero import tools
 
found_device: device.Device = None
 
# デバイスが見つかったときのコールバック
def on_device_found(device: device.Device):
    global found_device
    try:
        print(device.address)
        print(device.name)
        if (device.name == 'My iPhone'):
            found_device = device
    except:
        print('Error')
 
 
def main():
    # Bluetoothドングルの取得
    dongles = adapter.list_adapters()
    print('dongles available: ', dongles)
    dongle = adapter.Adapter(dongles[0])
 
    # Bluetoothドングルの電源が切れている場合は、電源を入れる
    if not dongle.powered:
        dongle.powered = True
        print('Now powered: ', dongle.powered)
    print('Start discovering')
 
    # デバイスが見つかったときのコールバック
    dongle.on_device_found = on_device_found
 
    # デバイスのスキャン開始
    dongle.nearby_discovery(timeout=20)
 
    # デバイスが見つかったら、ペアリング
    if (found_device != None) :
        found_device.pair()
    
 
    # dongle.powered = False
 
 
if __name__ == '__main__':
    print(__name__)
    logger = tools.create_module_logger('adapter')
    logger.setLevel(logging.DEBUG)
    main()