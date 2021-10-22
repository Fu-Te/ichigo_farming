import RPi.GPIO as GPIO
import dht11
import time
import datetime
import csv
import ambient
import tkinter

#GPIOの初期化
#GPIO.setwarnings(True)
#GPIO.setmode(GPIO.BCM)

#データの読み込みで14ピンを使う
#instance = dht11.DHT11(pin=14)
#tkinterで使えるようにしたら面白いかも

#ambientの設定
ambi=ambient.Ambient(41563,'ba0c12f7851e4dad')



def sensor_settings():
	#GPIO初期化
	GPIO.setwarnings(True)
	GPIO.setmode(GPIO.BCM)
	global instance
	instance = dht11.DHT11(pin=14)

def take_temp_humid():
	#グローバル関数にすることで他の関数内でも利用可能，変数(result.temperature,result.humidityが変化するように．)
	global result
	result = instance.read()
	if result.is_valid():
		if result.humidity != 0 or result.temperature != 0:

			print('日時:' + str(datetime.datetime.now()))
			print('気温: %-3.1f C' % result.temperature)
			print('湿度: %-3.1f %%' % result.humidity)
		else:
			print('湿度温度取得失敗')

def send_ambi():
	if result.humidity != 0 or result.temperature != 0:
		r=ambi.send({'d1':result.temperature, 'd2':result.humidity})
		print('ambiへ送信')
	else:
		print('温度湿度取得失敗したため送信しません．')

def store_data():
	with open('tem_humid.csv','a',newline='') as f:
		if result.humidity != 0 or result.temperature != 0:
			writer=csv.writer(f,lineterminator='\n')
			writer.writerow([datetime.datetime.now(),result.temperature,result.humidity])
			print("csv保存成功")

def gui_start():
	app.geometry(
		'400x400'
	)
	app.title(
		'センサ'
	)

def gui_label():
	label1=tkinter.Label(
		app,
		font = ('System',30),
		text = '温度: %-3.1f C' %result.humidity
	)
	label2=tkinter.Label(
		app,
		font = ('System',30),
		text = '湿度: %-3.1f %%' % result.humidity
	)


sensor_settings()
try:
	while True:
		take_temp_humid()
		send_ambi()
		store_data()

		time.sleep(6)

except KeyboardInterrupt:
	print('Cleanup')
	GPIO.cleanup()
