from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "8891techa0128"

@app.route("/")
def index():
    if "visit_count" not in session:
        session["visit_count"] = 1
    else:
        session["visit_count"] += 1
    return render_template("index.html", visits_count = session["visit_count"])

@app.route("/destroy-session")
def clear_session():
    # session.pop("visit_count")
    session.clear()
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)