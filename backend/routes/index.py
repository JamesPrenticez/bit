from flask import render_template, Blueprint

import sys
sys.path.append('./functions')

from functions.test import sum

class Index:
    def __init__(self):
        self.index = self.create_index()

    def create_index(self):
        index_page = Blueprint("index", __name__)
                
        @index_page.route("/", methods=['GET','POST'])
        @index_page.route("/home", methods=['GET','POST'])
        
        def index():

          result = sum(10, 90)

          return render_template("index.html", result=result)
        
        return index_page