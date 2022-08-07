from flask import Flask, app, session, request, redirect, url_for, render_template
from datetime import timedelta

app = Flask(__name__)
app.jinja_env.cache = {}
app.secret_key = "I68#nhKm6Z&@ZPB6!WxqA7NPE"
app.permanent_session_lifetime = timedelta(hours=12)

@app.route("/")
def home():
  return render_template("index.html", content=["BTC", "ETH", "XRP"])

@app.route("/dashboard/")
def dashboard():
  return render_template("dashboard.html", content=["BTC", "ETH", "XRP"])

@app.route("/login/", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    session.permanent = True
    user = request.form["username"]
    session["user"] = user
    return redirect(url_for("user"))
  else:
    if "user" in session:
      return redirect(url_for("user")) 

    return render_template("login.html")

@app.route("/logout/")
def logout():
  session.pop("user", None)
  return redirect(url_for("login"))

@app.route("/user/")
def user():
  if "user" in session:
    user = session["user"]
    return f"<h1>{user}</h1>"
  else:
    return redirect(url_for("login"))

if __name__ == "__main__":
  app.run(debug=True)