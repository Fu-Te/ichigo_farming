from flask import Flask
from .. import tem_humid
app = Flask(__name__)
@app.route('/')
#def hello_world():
#	return 'hello_world'
def main():
	return render_template('main.html')


app.run(port=8000,debug=True)