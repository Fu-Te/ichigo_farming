from flask import Flask,render_template
from tem_humid import take_temp_humid
from tem_humid import sensor_settings


app = Flask(__name__)
@app.route('/')
def main():
	sensor_settings()
	take_temp_humid()
	temp = result.temperature
	humid = result.humidity
	return render_template('main.html',temp=temp,humid=humid)


if __name__=='__main__':
	app.run(port=8000,debug=True)