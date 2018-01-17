from app import app 
from flask import render_template 
import re

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index') 

def index():
    return render_template('index.html', methods = ['GET', 'POST'])
