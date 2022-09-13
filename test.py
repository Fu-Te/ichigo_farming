import json

json_file = open('settings.json', 'r')
json_data = json.load(json_file)

bt_addrs = []

for addr in json_data.values():
    bt_addrs.append(addr)
    


print(bt_addrs)