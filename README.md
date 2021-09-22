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


1.ペリフェラルはセントラルからの接続待ち状態としてアドバタイズという状態になる．アドバタイズは，ペリフェラル機器が’どこにいるか’を伝える．アドバタイズの発信周期は自由に設定できる．このアドバタイズにはペリフェラル機器の名前や属性データを含めて発信できる．また，アドバタイズはブロードキャスト通信である．

2.セントラル機器はスキャンをすることで，アドバタイズを受信し，周囲にどのようなペリフェラル機器がいるかを知ることができる．複数のペリフェラル機器がアドバタイズを発信している場合は，セントラル機器はそれぞれのアドバタイズを受信して，周囲にいる複数のペリフェラル機器を認識することができる．受信した電波の強さに関する情報も得ることができ，ペリフェラル機器との距離感を知ることができる．

3.セントラル機器は見つけたペリフェラル機器の中から１対１の通信接続をしたい相手を選び，接続要求を送信することができる．ペリフェラルはアドバタイズを発信した後，少しの時間，自分に対する接続要求が飛んでこないか待っている．接続要求を受信すると，アドバタイズをやめて１対１の接続通信に切り替える．
<img width="444" alt="17f456767dd1c28a38ae8ab114896409" src="https://user-images.githubusercontent.com/37261985/134323698-d46a82d9-8fb8-48a1-bbc6-921cfabf7c15.png">（猿でもわかるBLEより）



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

# これから実装したいこと

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

BluetoothMeshについて:https://www.musen-connect.co.jp/blog/course/trial-production/bluetooth5-2/
猿でもわかるBLE:https://www.musen-connect.co.jp/blog/course/trial-production/ble-beginner-1/
webページで確認センサデータを確認できるようになったら面白いかも？　参考:https://www.iotstarters.com/raspberry-pi-flask-web-server-with-dht11/




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
