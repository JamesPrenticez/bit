import os
from flask import Flask

from routes.index import Index
from routes.api import Api

################################################
### ENVIROMENT VARIABLES
################################################
from dotenv import load_dotenv
load_dotenv()
BINANCE_PUBLIC_API_KEY = os.getenv("BINANCE_PUBLIC_API_KEY")
BINANCE_SECRET_API_KEY = os.getenv("BINANCE_SECRET_API_KEY")
BITMEX_PUBLIC_API_KEY =  os.getenv("BITMEX_PUBLIC_API_KEY")
BITMEX_SECRET_API_KEY = os.getenv("BITMEX_SECRET_API_KEY")

################################################
### CREATE FLASK APP
################################################
app = Flask(__name__, static_folder="../frontend/public/", template_folder="../frontend/public/")

################################################
### PAGES / ROUTES / BLUEPRINTS
################################################
index = Index()
api = Api()

app.register_blueprint(index.index)
app.register_blueprint(api.api)

if __name__ == '__main__':
    app.run(use_reloader=True, port=3000, threaded=True, debug=True)