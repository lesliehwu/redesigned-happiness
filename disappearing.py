from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja")
def ninjas():
    return render_template("ninja.html")

@app.route("/ninja/<color>")
def which_ninja(color):
    if color == "blue":
        return render_template("blue.html")
    if color == "orange":
        return render_template("orange.html")
    if color == "red":
        return render_template("red.html")
    if color == "purple":
        return render_template("purple.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"),404

app.run(debug = True)
