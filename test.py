import json
# ビーコンのアドレス一覧(自分の端末以外のアドレスを指定)
json_file = open('settings.json', 'r')
json_data = json.load(json_file)

bt_addrs = []

for bt_addr in json_data.values():
    bt_addrs.append(bt_addr)

print(bt_addrs)