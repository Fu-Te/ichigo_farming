# 日本語
# はじめに
このレポジトリーではRaspberrypiで気温、湿度、土壌湿度、日照などをセンサで計測し、Bluetooth接続を用いて、他の端末と接続し、制御、通知、データ収集及び解析を行う目的で作られたものです。

The purpose of this repository is to use the Raspberrypi to measure temperature, humidity, soil humidity, sunshine, etc. with sensors and connect to other devices using Bluetooth connectivity for control, notification, data collection and analysis.

# そもそもBLEどうやってつかうの？
BLE通信ではCentral(セントラル)とPeripheral(ペリフェラル)の２種類の役割があって，この二者間でやりとりがされるらしい．
セントラルは通信を制御する役割を持っていて，BLEではセントラルがペリフェラルに対して要求を出すことでデータ通信が行われる．一般的にはセントラルがスマホとかPC
ペリフェラルはセントラルからの要求に応える形で通信を行う．通信の制御機能は持ってない．
つまり，コードを書くときには，送信側（データ取得等）と受信側で２個コードを書く必要があるっぽい．
UUIDという識別子があって，それを指定することでセントラルはペリフェラル内の情報にアクセスできる．

セントラルがペリフェラルに対して接続要求をし，ペリフェラルからセントラルへ接続確立，データのやりとりをする．接続を終了する際はセントラルからペリフェラルへ接続切断をしらせる．



https://tomosoft.jp/design/?p=41722
https://www.denshi.club/cookbook/sensor/co2/co210ble.html

[参考](https://houwa-js.co.jp/2018/06/20180629/)
# 気温、湿度
気温、湿度はDHT11を用いて計測します。
コードは[こちら](https://github.com/szazo/DHT11_Python)を参考に書いています。
The code is written with reference to [here](https://github.com/szazo/DHT11_Python).
GND:6pin
DATA:8pin
VCC:2pin

これからはユーザから要請があったときにcsvファイルを送信する方法
１時間ごとにcsvファイルをメイン機に送信する機能
異常なデータがとれた際にデータを送信する方法
ambientを使ってデータをクラウドに送信し，グラフ化

[bluepy](https://github.com/IanHarvey/bluepy)
bluetoothでの通信はbluepyを用いる
[bleak](https://pypi.org/project/bleak/)を使う，
pybluezを使う方法があるっぽい？
全てのOSで使えるという点ではBleakがいいっぽい．
bleakを使う場合はこれまでのゼミの活動をもう一度チェックしてみると楽に進むかも？
授業で取り扱ったスライド2年後期第２回〜




# 使い方
raspberrypi上で

```
$ git clone https://github.com/Fu-Te/ichigo_farming.git
```
次にディレクトリ移動
```
$ cd ichigo_farming
```
必要なものを入れる
```
$ sudo apt-get install libglib2.0-dev
```
```
$ pip install git+https://github.com/AmbientDataInc/ambient-python-lib.git
```
次のコマンドで仮想環境に入ります．それによってpip等でインストールする手間を省ける（多分
```
$ source venv/bin/activate
```


以下のコマンドでBLEペリフェラルのアドレスを探す(central上で実行)
```
$ sudo python3 discover.py
```
アドバタイジングしているBLEペリフェラルを探し，見つけ，Device Addrをメモしておく．
explorer.pyのコードのアドレス部分を取得したアドレスに変更する．
そして
```
$ python3 explorer.py
```
を実行し，通信できることを確認する．
# English

# How does BLE work in the first place?
In BLE communication, there are two types of roles, Central and Peripheral, and they communicate with each other.
Central has the role of controlling the communication, and in BLE, data communication is performed by Central issuing requests to Peripheral. In general, the central is a smartphone or PC.
Peripherals communicate in response to requests from the central. It does not have any function to control the communication.
In other words, when you write code, you need to write two codes, one for the sending side (data acquisition, etc.) and one for the receiving side.
There is an identifier called UUID, and by specifying it, the central can access the information in the peripheral.

The central makes a connection request to the peripheral, the peripheral establishes a connection to the central, and data is exchanged. When the connection is terminated, the central sends a disconnection message to the peripheral.



https://tomosoft.jp/design/?p=41722
https://www.denshi.club/cookbook/sensor/co2/co210ble.html

[Reference](https://houwa-js.co.jp/2018/06/20180629/)
# Temperature and humidity
The temperature and humidity are measured using DHT11.
The code is written with reference to [here](https://github.com/szazo/DHT11_Python).
The code is written with reference to [here](https://github.com/szazo/DHT11_Python).
GND:6pin
DATA:8pin
VCC:2pin

From now on, how to send a csv file when requested by the user
Function to send csv file to the main unit every hour.
How to send data when abnormal data is obtained.
Send data to the cloud using ambient and graph it.

[bluepy](https://github.com/IanHarvey/bluepy)
Use bluepy to communicate via bluetooth
Using bleak.
There seems to be a way to use pybluez?
Bleak seems to be better in that it can be used on all OS.
If you want to use bleak, you should check the activities of the seminar so far.
Slides from the second semester of the second year of the class




# How to use
On raspberrypi

```
$ git clone https://github.com/Fu-Te/ichigo_farming.git
```
Then move the directory
```
$ cd ichigo_farming
```
Put in what you need.
```
$ sudo apt-get install libglib2.0-dev
```
```
$ pip install git+https://github.com/AmbientDataInc/ambient-python-lib.git
```
The following command enters the virtual environment. It will save you the trouble of installing it with pip (maybe).
```
$ source venv/bin/activate
```


Find the BLE peripheral addr with the following command (run on central)
```
$ sudo python3 discover.py
```
Find and locate the BLE peripheral you are advertising, and note down the Device Addr.

Replace the addr with the one you got before and then execute the following command to see if we can communicate.
```
$ sudo python3 explorer.py
```

That is it for now.