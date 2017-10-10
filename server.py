from flask import Flask, render_template, request, redirect, flash


app = Flask(__name__)
app.secret_key = "WAOW"
@app.route('/')
def root():
    return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def process():
    name = request.form['name']
    if len(name) < 1:
        flash("That's not a real name")
    else:
        flash("Cool {} is a real name.".format(name))

    location = request.form['location']
    language = request.form['language']
    bobo = request.form['bobo']
    if len(bobo) < 1:
        flash("no comment.")
    elif len(bobo) > 120:
        flash("You actually expect us to read all that?")
    return render_template("results.html", name = name, location = location, language = language, bobo = bobo)
    return redirect("/")



app.run(debug = True)