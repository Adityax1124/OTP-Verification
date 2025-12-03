from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("password")
        generated_password = request.form.get("generated")  # Get the hidden password
        if user_input and int(user_input) == int(generated_password):
            return redirect("/verified")
    # Generate new password for GET request
    password = random.randint(100000, 999999)
    return render_template("index.html", password=password)

@app.route("/verified")
def verified():
    return render_template("verified.html")


