#tkinterを用いたアプリ（テスト開発用）
import tkinter
from discover import scan

root = tkinter.Tk()
#タイトルと大きさの設定
root.title('Test')
root.geometry("400x300")

#BLEデバイスのScanボタンの作成
Button1=tkinter.Button(text=u'Scan',width=50)
Button1.bind('<Button-1>',scan)
Button1.pack()

Button2=tkinter.Button(text=u'温度・湿度',width=50)
#Button2.bind('<Button-2>',take_temp_humid)
Button2.pack()

#終了宣言
root.mainloop()