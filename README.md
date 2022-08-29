# 日本語
# 初めに
本レポジトリは卒論に向けた開発を行うためのものである．

# システムの概要
BLEとBlockchainを組み合わせたシステムを構築する．
Raspberrypiは4台程度用意し，相互通信をBLEを用いて実現する．
RaspberrypiをBLEビーコンとし，スマートフォンやノートパソコンのBLEブロードキャストをキャッチする．キャッチした情報をAESで暗号化し，BLE経由でデバイス間で共有する．共有されたデータをブロックにのせ，以前のハッシュ値と見比べることでチェーンを作成する．

# blockchain
blockchainフォルダでは，ブロックとチェーンを作成し，情報を載せるためのブロックチェーンを実装する．

ブロックチェーンをテストするためのDockerを作成している途中である．


# ble

Raspberrypi同士の通信ではl2cap_client.pyとl2cap_server.pyを利用する．
discover.pyでbleブロードキャストをキャッチする．


#　環境構築
Raspberrypi上で
```
$ sudo apt-get install git
$ git clone https://github.com/Fu-Te/BLE_Blockchain
$ cd BLE_Blockchain
$ sudo apt-get install libatlas-base-dev
$ sudo apt-get install libjasper-dev
$ sudo apt-get install bluetooth libbluetooth-dev
$ pip install -r requirements.txt
```
上記コマンドを行なうと環境構築が完了する．

# 使い方
```
$ python3 main.py
```
上記コマンドを実行することで利用することが可能．

# pytest
pytestを用いたテストを考えている