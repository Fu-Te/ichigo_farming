from flask import Flask,render_template
from tem_humid import take_temp_humid


app = Flask(__name__)
@app.route('/')
#def hello_world():
#	return 'hello_world'
def main():

	return render_template('main.html')



app.run(port=8000,debug=True)