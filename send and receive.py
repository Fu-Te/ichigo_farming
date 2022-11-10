　
from concurrent.futures import ThreadPoolExecutor

def toTwo(bt_addrs, data):

　　""" 
  
     アドレス番号1（仮）から2を送信先に指定しデータを送信することが出来る
     
    Parameters
    ----------
    
    bt_addrs : bluetoothアドレスが格納されたリスト
    data : 送りたい情報
    
    
    """
 
    client_thread = threading.Thread(
        target=l2cap_client(
        bt_addrs[0], send_data_list))
    
def toThree(bt_addrs, data):
　　""" 
  
     アドレス番号1（仮）から3を送信先に指定しデータを送信することが出来る
     
    Parameters
    ----------
    
    bt_addrs : bluetoothアドレスが格納されたリスト
    data : 送りたい情報
    
    
    """
    client_thread=threading.Thread(
        target=l2cap_client(
        bt_addrs[1], send_data_list))
        

def toFour(bt_addrs, data):
　　""" 
  
     アドレス番号1（仮）から4を送信先に指定しデータを送信することが出来る
     
    Parameters
    ----------
    
    bt_addrs : bluetoothアドレスが格納されたリスト
    data : 送りたい情報
    
    
    """
    client_thread=threading.Thread(
        target=l2cap_client(
        bt_addrs[2], send_data_list))

# 送信はまとめて
def SEND():
    """ 
  
     toTwo,toThree,toFourを並列で処理する
     (max_worker=3)は最大3つまで並列処理出来ることを表している
  
    """
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(toTwo())
        executor.submit(toThree())
        executor.submit(toFour())

