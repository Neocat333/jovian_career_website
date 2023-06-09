from flask import Flask, render_template
# see https://flask.palletsprojects.com/en/2.2.x/quickstart/

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('home.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)