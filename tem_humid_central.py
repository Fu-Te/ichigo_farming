#受信側のコード
import time
from pybleno import *
 
TOMOSOFT_SERVICE_UUID = '0000fff0-0000-1000-8000-00805f9b34fb'
READ_CHARACTERISTIC_UUID = '0000fff0-0000-1000-8000-00805f9b34fb'
SETTING_CHARACTERISTIC_UUID = '0000fff3-0000-1000-8000-00805f9b34fb'
COMMAND_CHARACTERISTIC_UUID = '0000fff4-0000-1000-8000-00805f9b34fb'
 
 
class ReadCharacteristic(Characteristic):
    def __init__(self):
        Characteristic.__init__(self, {
            'uuid': READ_CHARACTERISTIC_UUID,
            'properties': ['read', 'notify'],
            'value': None
        })
 
        self._value = 0
        self._updateValueCallback = None
 
    def onSubscribe(self, maxValueSize, updateValueCallback):
        print('ApproachCharacteristic - onSubscribe')
        self._updateValueCallback = updateValueCallback
 
    def onUnsubscribe(self):
        print('ApproachCharacteristic - onUnsubscribe')
        self._updateValueCallback = None
 
 
class SettingCharacteristic(Characteristic):
    def __init__(self):
        Characteristic.__init__(self, {
            'uuid': SETTING_CHARACTERISTIC_UUID,
            'properties': ['write'],
            'value': None
        })
 
    def onWriteRequest(self, data, offset, withoutResponse, callback):
        callback(self.RESULT_SUCCESS)
 
 
class CommandCharacteristic(Characteristic):
    def __init__(self):
        Characteristic.__init__(self, {
            'uuid': COMMAND_CHARACTERISTIC_UUID,
            'properties': ['write'],
            'value': None
        })
 
    def onWriteRequest(self, data, offset, withoutResponse, callback):
        callback(self.RESULT_SUCCESS)
 
 
def onStateChange(state):
    print('on -> stateChange: ' + state)
    if (state == 'poweredOn'):
        bleno.startAdvertising('TomoSoftx', [TOMOSOFT_SERVICE_UUID])
    else:
        bleno.stopAdvertising()
 
 
def onAdvertisingStart(error):
    print('on -> advertisingStart1: ' + ('error ' + error if error else 'success'))
    if not error:
        print('onAdvertisingStart')
        bleno.setServices([
            BlenoPrimaryService({
                'uuid': TOMOSOFT_SERVICE_UUID,
                'characteristics': [
                    tomosoftCharacteristic_cmd,
                    tomosoftCharacteristic_read,
                    tomosoftCharacteristic_set
                ]
            })
        ])
 
 
def onWriteRequest_cmd(data, offset, withoutResponse, callback):
    global counter
    counter += 1
    tomosoftCharacteristic_cmd._value = counter
    if tomosoftCharacteristic_read._updateValueCallback:
        print('Sending notification with value-cmd : ' + str(tomosoftCharacteristic_cmd._value))
        notificationBytes = str(tomosoftCharacteristic_cmd._value).encode()
        tomosoftCharacteristic_read._updateValueCallback(notificationBytes)
 
 
def onWriteRequest_set(data, offset, withoutResponse, callback):
    global counter
    counter += 1
    tomosoftCharacteristic_cmd._value = counter
    if tomosoftCharacteristic_read._updateValueCallback:
        print('Sending notification with value-set : ' + str(tomosoftCharacteristic_cmd._value))
        notificationBytes = str(tomosoftCharacteristic_cmd._value).encode()
        tomosoftCharacteristic_read._updateValueCallback(notificationBytes)
 
 
if __name__ == '__main__':
    bleno = Bleno()
    bleno.on('stateChange', onStateChange)
    bleno.on('advertisingStart', onAdvertisingStart)
    tomosoftCharacteristic_read = ReadCharacteristic()
    tomosoftCharacteristic_cmd = CommandCharacteristic()
    tomosoftCharacteristic_set = SettingCharacteristic()
    tomosoftCharacteristic_cmd.on('writeRequest', onWriteRequest_cmd)
    tomosoftCharacteristic_set.on('writeRequest', onWriteRequest_set)
    bleno.start()
    counter = 0
 
    while True:
        time.sleep(1)