from flask import Flask,render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/user")
def landing():
    return render_template('landingpage.html')


@app.route('/stock')
def stock():
    return render_template('stock.html')


if __name__ == "__main__":
    app.run(debug=True)