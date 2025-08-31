import os

from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def form_submission():
    name = request.form["name"]
    email = request.form['email']
    message = request.form['message']
    with open("form-submission.txt", 'a') as f:
        f.write(f"\n\n\n\nNew Submission\nName: {name}\nEmail: {email}\nMessage: {message}")
    return redirect(url_for('success'))


@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/store/blackcastle")
def blackcastle():
    return render_template("/store-item-1.html")

@app.route("/store/faces")
def faces():
    return render_template("/store-item-2.html")

@app.route("/store/lake")
def lake():
    return render_template("/store-item-3.html")

@app.route("/store/sheep")
def sheep():
    return render_template("/store-item-4.html")
@app.route("/store/bmx")
def bmx():
    return render_template("/store-item-5.html")
@app.route("/store/TaSe")
def TaSe():
    return render_template("/store-item-6.html")
@app.route("/store/bird")
def bird():
    return render_template("/store-item-7.html")
@app.route("/store/lighthouse")
def lighthouse():
    return render_template("/store-item-8.html")
@app.route("/store/hills")
def hills():
    return render_template("/store-item-9.html")
@app.route("/store/evischen")
def evischen():
    return render_template("/store-item-10.html")

if __name__ == "__main__":
    app.run(debug=True, port=9101)
