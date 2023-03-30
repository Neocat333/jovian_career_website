from flask import Flask
# see https://flask.palletsprojects.com/en/2.2.x/quickstart/

app = Flask(__name__)

@app.route("/")
def hello():
	return 'hello'

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)