from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "8891techa0128"

@app.route("/")
def index():
    if "visit" and "counter" not in session:
        session["visit"] = 0
        session["counter"] = 0
    else:
        session["visit"] += 1
        session["counter"] += 1

    return render_template("index.html", visit = session["visit"], counter = session["counter"])

@app.route("/reset-counter")
def reset_visits():
    session["visit"] = 0
    return redirect("/")

@app.route("/increment-by-two")
def increment_by_two():
    if "visit" and "counter" in session:
        session['visit'] += 1
        session["counter"] += 1
    return redirect("/")

@app.route("/increment-by-val", methods = ["POST"])
def increment_by_val():
    increment_val = int(request.form["increment_value"])
    session["counter"] += increment_val
    return redirect("/")

@app.route("/reset-session")
def clear_session():
    # session.pop("visits")
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)