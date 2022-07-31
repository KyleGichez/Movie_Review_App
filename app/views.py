from flask import render_template
from app import app

@app.route('/')
def index():
    message = 'Hello Sexy Ms Dollar Baby, How is you experience with flask so far?'
    return render_template('index.html', message = message)