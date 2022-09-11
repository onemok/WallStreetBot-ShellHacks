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

@app.route("/dashboard", methods = ['POST', 'GET'])
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

@app.route("/dashboarddisplay", methods = ['POST', 'GET'])
def dashboard_display():
    stock_name = request.form.get("stock")
    direction = WSBMLAI.call_stock(str(stock_name))
    chart_address = f"5y{stock_name}.png"
    output = ""
    if direction == float(0):
        output += f"Our ML Model believes, with 65% accuracy, {stock_name} will close lower tomorrow than it did today"
    else:
        output += f"Out ML Model believes, with 65% accuracy, {stock_name} will close higher tomorrow than it did today"

    return render_template("dashboarddisplay.html", answer = output, graph = chart_address)

#@app.route("/", methods = ["POST", "GET"])
#def trade():
    #stock_name = request.form("stock")
    #go, acc = WSBMLAI.call_stock(stock_name)
    #return go, acc


if __name__ == '__main__':
    app.run()

    #We the Prophet of Profit