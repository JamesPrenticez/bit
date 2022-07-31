from flask import Flask, render_template

app = Flask(__name__, static_folder="../frontend/public/", template_folder="../frontend/public/")

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(use_reloader=True, port=3000, threaded=True, debug=True)