from flask import Flask, request, url_for, render_template
import WSBMLAI

app = Flask(__name__, template_folder="../Frontend/templates")

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()