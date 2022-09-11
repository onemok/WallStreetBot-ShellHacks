from crypt import methods
from flask import Flask, request, url_for, render_template
import WSBMLAI

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route("/signup", methods = ['POST', 'GET'])
def signup():
    return render_template("signup.html")

@app.route("/signup/dashboard", methods = ['POST', 'GET'])
def dashboard():
    return render_template("dashboard.html")

@app.route("/trade", methods = ['POST', 'GET'])
def trade():
    return render_template("trade.html")

@app.route("/crypto", methods = ['POST', 'GET'])
def crypto():
    return render_template("crypto.html")

@app.route("/papertrading", methods = ['POST', 'GET'])
def papertrading():
    return render_template("papertrading.html")

@app.route("/aboutus", methods = ['POST', 'GET'])
def aboutus():
    return render_template("aboutus.html")

@app.route("/signup/dashboard", methods = ['POST', 'GET'])
def dashboard_display():
    stock_name = request.form("stock")
    direction = WSBMLAI.call_stock(stock_name)
    return direction

#@app.route("/", methods = ["POST", "GET"])
#def trade():
    #stock_name = request.form("stock")
    #go, acc = WSBMLAI.call_stock(stock_name)
    #return go, acc


if __name__ == '__main__':
    app.run()

    #We the Prophet of Profit