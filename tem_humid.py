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

