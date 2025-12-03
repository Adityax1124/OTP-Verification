from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Store password globally (reset each page load)
password = random.randint(100000, 999999)

@app.route('/', methods=['GET', 'POST'])
def index():
    global password
    if request.method == 'POST':
        user_input = request.form.get('password')
        if user_input and user_input.isdigit() and int(user_input) == password:
            return redirect(url_for('verified'))
        else:
            return render_template('index.html', password=password, error="Invalid Password")
    
    # Refresh password each page load
    password = random.randint(100000, 999999)
    return render_template('index.html', password=password)

@app.route('/verified')
def verified():
    return render_template('verified.html')

if __name__ == "__main__":
    app.run(debug=True)



