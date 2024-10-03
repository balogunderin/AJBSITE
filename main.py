from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/resume")
def cv():
    return render_template("resume.html")

@app.route("/media")
def interviews():
    return render_template("media.html")


if __name__ == "__main__":
    app.run(debug=True)