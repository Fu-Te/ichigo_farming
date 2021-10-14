#tkinterを用いたアプリ（テスト開発用）
import tkinter
from discover import scan

root = tkinter.Tk()
#タイトルと大きさの設定
root.title('Test')
root.geometry("1200x800")

#BLEデバイスのScanボタンの作成
Button1=tkinter.Button(text=u'Scan',width=50)
Button1.bind('<Button-1>',scan())
Button1.pack()

#終了宣言
root.mainloop()