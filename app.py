from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session

def get_random_number():
    return random.randint(100000, 999999)

@app.route("/", methods=["GET", "POST"])
def index():
    if "password" not in session:
        session["password"] = get_random_number()
    
    result = ""
    if request.method == "POST":
        try:
            user_input = int(request.form["user_input"])
            if user_input == session["password"]:
                return redirect(url_for("verified"))
            else:
                result = "Invalid Password ❌"
        except ValueError:
            result = "Please enter a valid number"
    
    return render_template("index.html", password=session["password"], result=result)

@app.route("/verified")
def verified():
    # Reset password for next loop
    session.pop("password", None)
    return render_template("verified.html")

if __name__ == "__main__":
    app.run(debug=True)
