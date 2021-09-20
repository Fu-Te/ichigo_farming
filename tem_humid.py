import RPi.GPIO as GPIO
import dht11
import time
import datetime
import csv
import ambient

#GPIOの初期化
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

#データの読み込みで14ピンを使う
instance = dht11.DHT11(pin=14)

#ambientの設定
ambi=ambient.Ambient(41563,'ba0c12f7851e4dad')

def take_temp_humid():
	result = instance.read()
	if result.is_valid():
		print('日時:' + str(datetime.datetime.now()))
		print('気温: %-3.1f C' % result.temperature)
		print('湿度: %-3.1f %%' % result.humidity)

def send_ambi():
	result = instance.read()
	r=ambi.send({'d1':result.temperature, 'd2':result.humidity})
	print('ambiへ送信')

def store_data():
	result = instance.read()
	with open('tem_humid.csv','a',newline='') as f:
		writer=csv.writer(f,lineterminator='\n')
		writer.writerow([datetime.datetime.now(),result.temperature,result.humidity])

try:
	while True:
		take_temp_humid()
		send_ambi()
		store_data()

		time.sleep(2)

except KeyboardInterrupt:
	print('Cleanup')
	GPIO.cleanup()