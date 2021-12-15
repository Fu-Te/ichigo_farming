#tkinterを用いたアプリ（テスト開発用）
import tkinter
from discover import scan


class Application(tkinter.Frame):
	def __init__(self,root):
		super().__init__(root,width=420,height=320,borderwidth=4,relief='groove')
		self.pack()
		self.pack_propagate(0)
		self.root=root

	def create_widget(self):
		#部品の追加
		self.text_box=tkinter.Entry(self)
		self.text_box['width']=10
		self.text_box.pack()

	def input_hundler(self):
		text=self.text_box.get()


	def end_app(self):
		quit_btn=tkinter.Button(self)
		quit_btn['text']='閉じる'
		quit_btn['command']=self.root.destroy
		quit_btn.pack(side='bottom')


root = tkinter.Tk()
#タイトルと大きさの設定
root.title('Test')
root.geometry("800x600")

app=Application(root=root)
app.mainloop()

#BLEデバイスのScanボタンの作成
Button1=tkinter.Button(text=u'Scan',width=50)
Button1.bind('<Button-1>',scan())
Button1.pack()

Button2=tkinter.Button(text=u'温度・湿度',width=50)
#Button2.bind('<Button-2>',take_temp_humid)
Button2.pack()

#終了宣言
root.mainloop()