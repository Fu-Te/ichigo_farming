import ambient
import time
from get_tem_humid import sensor_settings,take_temp_humid,send_ambi,store_data,cleanup
#ambientの設定
ambi=ambient.Ambient(41563,'ba0c12f7851e4dad')
# センサーの初期設定
sensor_settings()

try:
	while True:
		take_temp_humid()
		send_ambi()
		store_data()

		time.sleep(6)

except KeyboardInterrupt:
	print('cleanup')
	cleanup()