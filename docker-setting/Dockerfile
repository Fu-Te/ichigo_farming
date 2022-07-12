FROM soodesune/python3-bluetooth

RUN apt-get update && apt-get install -y git wget

RUN pip install pandas bleak pybluez

WORKDIR /root

RUN git clone https://github.com/Fu-Te/BLE_Blockchain.git
