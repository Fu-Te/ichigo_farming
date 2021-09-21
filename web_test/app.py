from flask import Flask,render_template
from tem_humid import take_temp_humid,sensor_settings


app = Flask(__name__)
@app.route('/')
#def hello_world():
#	return 'hello_world'
def main():
	sensor_settings()
	take_temp_humid()
	return render_template('main.html',)


if name__=='__main__':

	app.run(port=8000,debug=True)