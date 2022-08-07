from flask import Flask, app, redirect, url_for, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

@app.route('/')
def home():
    return render_template('index.html', content=['BTC', 'ETH', 'XRP'])

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', content=['BTC', 'ETH', 'XRP'])

@app.route('/user/<name>/')
def user(name):
    return f"user: {name}"

@app.route('/admin/')
def admin():
    return redirect(url_for('user', name='Admin!'))

if __name__ == '__main__':
    app.run(debug=True)