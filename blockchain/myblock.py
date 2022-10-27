import datetime as dt
import json
import hashlib
import pandas as pd


class MyBlockChain(object):
    # ブロックチェーンを初期化する
    def __init__(self):
        self.chain = []

    # 新しいブロックを作成する
    def add_new_block(self, inp, outp):
        # トランザクションを生成する
        new_transaction = self.__create_new_transaction(inp, outp)

        # 前のブロックのハッシュを取得。最初だけ固定値
        if len(self.chain) > 0:
            prev_hash = self.chain[-1]['block_header']['tran_hash']
        else:
            prev_hash = "747bc42088cf0b3915982af289189e8f14d3325a7d594bc2d30a7014a536cb13"

        # トランザクションを元にブロックを生成して、チェーンに接続する
        new_block = {
            'block_index': len(self.chain) + 1,
            'block_time': dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'block_header': {
                'prev_hash': prev_hash,
                'tran_hash': self.__hash(prev_hash + self.__calc_tran_hash(new_transaction)),
            },
            'tran_counter': len(inp) + len(outp),
            'tran_body': new_transaction,
        }
        self.chain.append(new_block)
        return new_block

    # 新しいトランザクションを生成する
    def __create_new_transaction(self, inp, outp):
        new_transaction = {
            'input': inp,
            'output': outp,
        }
        return new_transaction

    # ハッシュ値を計算する。SortをTrueにしているのはハッシュの整合性維持のため
    def __calc_tran_hash(self, new_transaction):
        tran_string = json.dumps(new_transaction, sort_keys=True).encode()
        return self.__hash(tran_string)

    def __hash(self, str_seed):
        return hashlib.sha256(str(str_seed).encode()).hexdigest()

    # ブロックの内容を表示する
    def dump(self, block_index=0):
        if(block_index == 0):
            print(json.dumps(self.chain, sort_keys=False, indent=2))
        else:
            print(
                json.dumps(
                    self.chain[block_index],
                    sort_keys=False,
                    indent=2))


bc = MyBlockChain()


def test_make_blockchain():

    df1 = pd.read_csv("sample1.csv")
    df2 = pd.read_csv('sample2.csv')
    df3 = pd.read_csv('sample3.csv')
    df4 = pd.read_csv('sample4.csv')

    df = pd.concat([df1, df2])
    df = pd.concat([df, df3])
    df = pd.concat([df, df4])

    df_count = df['MAC'].value_counts().to_frame()
    df_count = df_count.reset_index()

    df['count'] = df_count['MAC']
    df.drop_duplicates(inplace=True)

    for gakuseki, mac, count in zip(df['Gakuseki'], df['MAC'], df['count']):
        if count >= 3:  # もう少しかっこよく50%以上を表現できると良い
            inp = {
                'GAC': gakuseki,
            }
            out = {
                'MAC': mac,
                'count': count
            }
            bc.add_new_block(inp, out)


def make_blockchain(receive_data_list):
    df_list = []
    for i in receive_data_list:
        df_list.append(i[0])
    df = pd.DataFrame()

    for i in df_list:
        df = pd.concat([df, i])

    df_count = df['MAC'].value_counts().to_frame()
    df_count = df_count.reset_index()

    df['count'] = df_count['MAC']
    df.drop_duplicates(inplace=True)
    df = df.sort_values('Gakuseki')

    for gakuseki, mac, count in zip(df['Gakuseki'], df['MAC'], df['count']):
        if count / len(df_list) >= len(df_list)/2:
            inp = {
                'GAK': gakuseki,
            }
            out = {
                'MAC': mac,
                'count': count
            }
            bc.add_new_block(inp, out)


test_make_blockchain()
bc.dump()
