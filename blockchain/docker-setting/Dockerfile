FROM ubuntu:20.04

# 必要そうなものをinstall

RUN apt-get update && apt-get install -y git wget

#任意バージョンのpython install
RUN apt-get install -y python3 python3-pip

#サイズ削減のため不要なものは削除
RUN apt-get autoremove -y

#必要なpythonパッケージをpipでインストール
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir jupyterlab

WORKDIR /root
RUN git clone https://github.com/Fu-Te/BLE_Blockchain

WORKDIR /BLE_Blockchain



#requirements.txtなら以下のように
RUN pip3 install -r ./requirements.txt