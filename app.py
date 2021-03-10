import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from flask import Flask,url_for,request,abort, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
	return render_template("index.html")
