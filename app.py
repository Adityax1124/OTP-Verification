from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = random.randint(100000, 999999)
    if request.method == "POST":
        user_input = request.form.get("password")
        if user_input and int(user_input) == int(request.form.get("generated")):
            return redirect("/verified")
    return render_template("index.html", password=password)

@app.route("/verified")
def verified():
    return render_template("verified.html")
