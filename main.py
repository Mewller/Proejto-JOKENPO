from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello, world"

@app.route("/costa_maldito")
def costa_maldito():
    return "costa seu bosta, eita RIMOU"


if __name__ == "__main__":
    app.run(debug=True)