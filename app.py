from flask import Flask, render_template, request, redirect, url_for, session
import random
import smtplib

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for session

EMAIL_ADDRESS = "adisinghx25@gmail.com"
EMAIL_PASSWORD = "fslf qbbe nenw efru"

def send_otp(email, otp):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    message = f"Subject: Your OTP\n\nYour OTP is {otp}"
    server.sendmail(EMAIL_ADDRESS, email, message)
    server.quit()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        otp = random.randint(100000, 999999)
        session["otp"] = str(otp)
        session["email"] = email
        send_otp(email, otp)
        return redirect(url_for("verify"))
    return render_template("home.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        user_otp = request.form.get("otp")
        if user_otp == session.get("otp"):
            return redirect(url_for("verified"))
        else:
            return render_template("verify.html", error="Invalid OTP")
    return render_template("verify.html", error=None)

@app.route("/verified")
def verified():
    return render_template("verified.html")

if __name__ == "__main__":
    app.run(debug=True)




