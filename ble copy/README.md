# how to use

```
$ sudo apt-get install libatlas-base-dev
$ sudo apt-get install libjasper-dev
$ sudo apt-get install bluetooth libbluetooth-dev
$ sudo python3 -m pip install pybluez
```

[bluetoothctlコマンド一覧](https://qiita.com/noraworld/items/55c0cb1eb52cf8dccc12)
[bluetoothmesh,Python](https://pypi.org/project/bluetooth-mesh/)
[bluetoothmeshセットアップ](https://www.logicalmixed.com/2019/01/29/meshctlbluez%e3%81%a7bluetooth-mesh%e3%82%92%e3%82%84%e3%81%a3%e3%81%a6%e3%81%bf%e3%82%8b/)

L2CAPというものが，Bluetooth通信において重要らしい（TCP,UDPみたいなもん）
[PyBlueZの使用参考例](https://github.com/karulis/pybluez/blob/master/examples/simple/l2capserver.py)