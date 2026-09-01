from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/representasi")
def representasi():
    return render_template("representasi.html")


@app.route("/ai")
def ai():
    return render_template("ai.html")


@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/programming")
def programming():
    return render_template("programming.html")


@app.route("/computational")
def computational():
    return render_template("computational.html")


@app.route("/cyber")
def cyber():
    return render_template("cyber.html")


@app.route("/battle")
def battle():
    return render_template("battle.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )