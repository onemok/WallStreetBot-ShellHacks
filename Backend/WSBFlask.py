from flask import Flask, request, url_for, render_template
import WSBMLAI

app = Flask(__name__, template_folder="../Frontend/templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route("/login/dashboard", methods = ['POST', 'GET'])
def dashboard():
    return render_template("dashboard.html")

@app.route("/login/dashboard", methods = ['POST', 'GET'])
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