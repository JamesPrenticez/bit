from flask import Flask, app, request, redirect, url_for, render_template

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = -1

@app.route("/")
def home():
  return render_template("index.html", content=["BTC", "ETH", "XRP"])

@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html", content=["BTC", "ETH", "XRP"])

@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    user = request.form["username"]
    return redirect(url_for("user", user=user))
  else:
    return render_template("login.html")

@app.route("/user/<user>")
def user(user):
  return f"<h1>{user}</h1>"

if __name__ == "__main__":
  app.run(debug=True)