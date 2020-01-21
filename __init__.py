
# coding: utf-8
from flask import Flask, render_template
from flask import request
import pandas as pd
import sys


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login_manager", methods=["POST"])
def login_manager():
    player_id = request.form["username"]
    return_message = f"ようこそ [{player_id}] さん"
    return return_message


if __name__ == "__main__":
    app.run(debug=True)

