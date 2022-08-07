from flask import Flask, app, session, request, redirect, url_for, render_template, flash
from datetime import timedelta

app = Flask(__name__)
app.jinja_env.cache = {}
app.secret_key = "I68#nhKm6Z&@ZPB6!WxqA7NPE"
app.permanent_session_lifetime = timedelta(hours=12)

@app.route("/")
def index():
  if "user" in session:
    user = session["user"]
    return redirect(url_for("dashboard"))
  else:
    return render_template("index.html")

@app.route("/home/")
def home():
  user = session["user"]
  return render_template("home.html", user=user)

@app.route("/dashboard/")
def dashboard():
  user = session["user"]
  return render_template("dashboard.html", user=user)

@app.route("/trades/")
def trades():
  user = session["user"]
  return render_template("trades.html", user=user)

@app.route("/account/")
def account():
  if "user" in session:
    user = session["user"]
    return render_template("account.html", user=user)
  else:
    flash("You are not logged in!")
    return redirect(url_for("login"))

@app.route("/settings/")
def settings():
  if "user" in session:
    user = session["user"]
    return render_template("settings.html", user=user)
  else:
    return redirect(url_for("login"))

@app.route("/login/", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    session.permanent = True
    user = request.form["username"]
    session["user"] = user
    flash("Login Succesfull!", "info")
    return redirect(url_for("account"))
  else:
    if "user" in session:
      flash("Already Logged In!", "info")
      return redirect(url_for("account")) 

    return render_template("login.html")

@app.route("/logout/")
def logout():
  user = session["user"]
  flash(f"User {user} has been logged out!", "info")
  session.pop("user", None)
  return redirect(url_for("login"))

if __name__ == "__main__":
  app.run(debug=True)