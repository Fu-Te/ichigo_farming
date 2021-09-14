# はじめに
このレポジトリーではRaspberrypiで気温、湿度、土壌湿度、日照などをセンサで計測し、Bluetooth接続を用いて、他の端末と接続し、制御、通知、データ収集及び解析を行う目的で作られたものです。

The purpose of this repository is to use the Raspberrypi to measure temperature, humidity, soil humidity, sunshine, etc. with sensors and connect to other devices using Bluetooth connectivity for control, notification, data collection and analysis.
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
$ pip install dht11 bluepy
```
```
$ sudo apt-get install libglib2.0-dev
```
```
$ pip install git+https://github.com/AmbientDataInc/ambient-python-lib.git
```
